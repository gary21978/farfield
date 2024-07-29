class Numerics:
    SampleNumber_Source: int = 61
    SampleNumber_Mask_X: int = 81
    SampleNumber_Mask_Y: int = 81
    SampleNumber_Wafer_X: int = 81
    SampleNumber_Wafer_Y: int = 81
    # Normailization
    Normalization_Intensity = 0
    # Imaging model => 'vector'  'scalar'
    ImageCalculationMode: str = 'vector'
    # Calculation model =>'abbe' 'hopkins'
    ImageCalculationMethod: str = 'abbe'
    # Truncation method for hopkins model => 'order' 'Threshold'
    Hopkins_SettingType: str = 'order'
    Hopkins_Order: int = 50
    Hopkins_Threshold: float = 0.95  # (0, 1)
    def __init__(self):
        pass