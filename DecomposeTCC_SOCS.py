import torch

def DecomposeTCC_SOCS(TCCMatrix_Stacked, FG_ValidSize, Nfg, numerics):
    Nf = Nfg[0]
    Ng = Nfg[1]
    
    U, S, _ = torch.svd(TCCMatrix_Stacked)
    if numerics.Hopkins_SettingType.lower() == 'order':
        socsNumber = min(numerics.Hopkins_Order, U.size(1) - 1)
    elif numerics.Hopkins_SettingType.lower() == 'threshold':
        rateThreshold = numerics.Hopkins_Threshold
        singularVector = torch.diag(S)
        totalSingular = torch.sum(singularVector)
        temp2 = 0
        socsNumber = U.size(1) - 1
        for i in range(len(singularVector) - 1):
            temp2 += singularVector[i]
            if temp2 > rateThreshold * totalSingular:
                socsNumber = i
                break
    else:
        raise ValueError('Error: Hopkins_SettingType should be order or threshold!')

    TCCMatrix_Kernel = torch.zeros(Ng, Nf, socsNumber, dtype=torch.complex64)
    temp2 = torch.zeros(Ng, Nf, dtype=torch.complex64)
    
    for i in range(socsNumber):
        temp1 = U[:, i].reshape(FG_ValidSize[1], FG_ValidSize[0])
        temp2[(Ng - FG_ValidSize[1] + 1) // 2 : (Ng + FG_ValidSize[1] + 1) // 2,
              (Nf - FG_ValidSize[0] + 1) // 2 : (Nf + FG_ValidSize[0] + 1) // 2] = temp1
        TCCMatrix_Kernel[:, :, i] = torch.fft.fftshift(temp2)

    diagS = S[0:socsNumber]
    diagS = diagS.reshape(1, 1, -1)
    TCCMatrix_Kernel = TCCMatrix_Kernel * torch.sqrt(diagS)

    return TCCMatrix_Kernel
