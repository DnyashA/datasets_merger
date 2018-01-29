from enum import Enum


class DefaultPathes(Enum):
    main_dat_path = 0
    sub_dat_path = 1
    main_markup = 2
    sub_markup = 3
    save_path = 4


class PathContainer(object):
    def __init__(self, pathes=None):
        if not pathes:
            # default pathes then
            self.pathes = ("/media/dnyasha/My Passport/Datasets/",
                           "/media/dnyasha/My Passport/Datasets/",
                           "candidates.csv",
                           "MSKCC RepeatCT Lesion notes for RIDER(reproceed).csv",
                           "/media/dnyasha/My Passport/Test/")
        else:
            self.pathes = pathes

        self.data_is_ok = True

        for path in self.pathes:
            try:
                file = open(path, 'r')
                file.close()
            except FileNotFoundError:
                print("File {0} does not exist".format(path))
                self.data_is_ok = False
                raise

    def _convert_pathes(self, pref_enum):
        return {pref_enum.main_dat_path: self.pathes[0],
                pref_enum.sub_dat_path: self.pathes[1],
                pref_enum.main_markup: self.pathes[2],
                pref_enum.sub_markup: self.pathes[3],
                pref_enum.save_path: self.pathes[4]}

    def get_pathes(self):
        if self.data_is_ok:
            return self._convert_pathes(DefaultPathes)
        else:
            return ()
