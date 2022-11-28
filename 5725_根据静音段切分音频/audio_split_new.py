# -- coding: utf-8 --
"""
@Project : pythonProject_wensi
@File : audio_split_new.py
@Author : wenjing
@Date : 2022/112/17 15:10


"""
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence
import sys
from pathlib import Path
sys.path.append(str(Path(f"{Path(__file__).parent.parent.parent}/Utilities")))


def main(wav_paths):
    for root, dirs, files in os.walk(wav_paths, topdown=False):
        for name in files:
            wav_path = os.path.join(root, name)
            print(wav_path)
            sound = AudioSegment.from_mp3(wav_path)
            loudness = sound.dBFS
            # print(loudness)
            chunks = split_on_silence(sound,
                                      # must be silent for at least half a second,沉默半秒
                                      min_silence_len=3000,  # 3s
                                      silence_thresh=-45,
                                      keep_silence=400
                                      )
            print('总分段：', len(chunks))
            for i, chunk in enumerate(chunks):
                chunk.export("{0}_{1}.wav".format(name.split('.')[0],i+1), format="wav")
                # print(i)


if __name__ == '__main__':
    main(r'C:\Users\Mawenjing\Desktop\wav')
    # wav_paths = Path(f"{sys.argv[1]}")
    # main(wav_paths)
