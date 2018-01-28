from Merger import Merger

if __name__ == '__main__':
    m = Merger("/media/dnyasha/My Passport/Datasets/", "/media/dnyasha/My Passport/Datasets/", "candidates.csv", "MSKCC RepeatCT Lesion notes for RIDER(reproceed).csv",
               "/media/dnyasha/My Passport/Test/", split=True)
    m.merge()