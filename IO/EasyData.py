# Copyright (c) 2014--2020 Tony (Muhammad) Yousefnezhad
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import numpy as np
import scipy.io as sio


def LoadEzData(Header=None,data=None):
    if Header is None:
        print("Please enter header file!")
        return None

    if not os.path.isfile(Header):
        print("Header file is not found!")
        return None

    try:
        Out = sio.loadmat(Header, appendmat=False)
        Int = Out["Integration"]
    except:
        print("Cannot load header file!")
        return None
    try:
        DataStruct = Int["DataStructure"][0]
        DataKey = list()
        for key in DataStruct:
            if data is None:
                DataKey.append(key)
            else:
                if key in data:
                    DataKey.append(key)

        if not len(DataKey):
            print("WARNING: No data key found!")
        else:
            if Out['DataFileType'][0][0] == 0:
                print("Data file type is NII.GZ")
            else:
                print("Data file type is EZMAT")
            for dkey in DataKey:
                X = None
                dfiles = np.array(Int[dkey[0] + "_files"])[0][0]
                for fdata in dfiles:
                    try:
                        if Out['DataFileType'][0][0] == 0:
                            import nibabel as nb
                            niiimgdata = nb.load(str.strip(os.path.dirname(Header) + "/" + fdata))
                            dat = np.transpose(niiimgdata.get_data())
                            X = dat if X is None else np.concatenate((X, dat))
                            del dat, niiimgdata
                        else:
                            dat = sio.loadmat(str.strip(os.path.dirname(Header) + "/" + fdata), appendmat=False)[dkey[0]]
                            X = dat if X is None else np.concatenate((X,dat))
                            del dat
                        print("Data %s is load!" % (fdata))
                    except Exception as e:
                        print(str(e))
                        return None
                Out[dkey[0]] = X
    except:
        print("DEBUG: Error in loading data files!")
        return None
    return Out
