class PEDSAlgorithmScore(object):
    def __init__(self, formId, NF_LOC_Child_Value, LOC_Child_Met_Reason, testStatus, expectedOutput, actualOutput,
                 rowNumber):
        self.formId = formId
        self.NF_LOC_Child_Value = NF_LOC_Child_Value
        self.LOC_Child_Met_Reason = LOC_Child_Met_Reason
        self.testStatus = "PASS" if testStatus else "FAIL"
        self.expectedOutput = expectedOutput
        self.actualOutput = actualOutput
        self.rowNumber = rowNumber
