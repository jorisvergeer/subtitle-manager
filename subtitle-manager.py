'''
Created on May 20, 2013

@author: joris
'''
import os
from fnmatch import fnmatch
import subprocess

def main():
    files = []
    for root, dirnames, filenames in os.walk("."):
        for filename in filenames:
            if (not "anime" in root) and (filename.endswith(".mp4") or filename.endswith(".mkv") or filename.endswith(".avi")):
                base = os.path.splitext(filename)[0];
                base = os.path.join(root, base);
                lowerbase = os.path.join(root, os.path.splitext(filename)[0].lower());
                
                print "Processing " + os.path.join(root,filename);
                
                if os.path.exists(base + ".srt"):
                    os.rename(base + ".srt", base + ".en.srt");
                    pass
                
                if os.path.exists(lowerbase + ".srt"):
                    os.rename(lowerbase + ".srt", base + ".en.srt");
                    pass

                if not os.path.exists(base + ".en.srt"):
                    subprocess.call(["subdownloader", "-c", "--lang=en", "--rename-subs", "-V", os.path.join(root,filename)]);
                    if os.path.exists(base + ".srt"):
                        os.rename(base + ".srt", base + ".en.srt");
                    if os.path.exists(lowerbase + ".srt"):
                        os.rename(lowerbase + ".srt", base + ".en.srt");
                    pass
                
                if not os.path.exists(base + ".nl.srt"):
                    subprocess.call(["subdownloader", "-c", "--lang=nl", "--rename-subs", "-V", os.path.join(root,filename)]);
                    if os.path.exists(base + ".srt"):
                        os.rename(base + ".srt", base + ".nl.srt");
                    if os.path.exists(lowerbase + ".srt"):
                        os.rename(lowerbase + ".srt", base + ".nl.srt");
                    pass
                pass
            pass
        pass
    pass

if __name__ == '__main__':
    main()
