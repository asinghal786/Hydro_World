class TrainingConfig:
    def __init__(
        self,
        gb_estimators=100,
        gb_learning_rate=0.1,
        svm_c=1.0,
        svm_kernel="rbf"
    ):
        self.gb_estimators = gb_estimators
        self.gb_learning_rate = gb_learning_rate
        self.svm_c = svm_c
        self.svm_kernel = svm_kernel
