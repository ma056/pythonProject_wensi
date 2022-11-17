'''
split_on_silence(sound,
        min_silence_len=600,
        silence_thresh=-60,
        keep_silence=400
    )
sound为声音文件。
min_silence_len=600,大于600毫秒的静音段则被认为是静音段，这个值如果设置过小，剪出来的声音会有卡顿感，设置在500秒左右是比较合适的。
silence_thresh=-60,这个值是声音多小才被认为是静音段。由于我的音频静音段声音几乎没有，所以我设置的比较小也不会出错，如果你们需要减除的静音段还是有一点声音的，那需要好好考虑设置多少合适。
keep_silence=400  这个值是剪切静音段保留多少静音段在有声音的音频段上，我设置的是400毫秒，如果太小，也会听着很变扭。如果设置太长，会有较长的静音段没剪掉。一般来说500左右合适。
'''

from pydub import AudioSegment
from pydub.silence import split_on_silence

sound = AudioSegment.from_mp3("QpDdHK2VAtc.wav")
loudness = sound.dBFS
# print(loudness)

chunks = split_on_silence(sound,
                          # must be silent for at least half a second,沉默半秒
                          min_silence_len=1000,
                          # consider it silent if quieter than -16 dBFS
                          silence_thresh=-45,
                          keep_silence=400
                          )
print('总分段：', len(chunks))

# 放弃长度小于2秒的录音片段
# for i in list(range(len(chunks)))[::-1]:
#     if len(chunks[i]) <= 2000 or len(chunks[i]) >= 10000:
#         chunks.pop(i)
# print('取有效分段(大于2s小于10s)：', len(chunks))

'''
for x in range(0,int(len(sound)/1000)):
    print(x,sound[x*1000:(x+1)*1000].max_dBFS)
'''

for i, chunk in enumerate(chunks):
    chunk.export("chunk{0}.wav".format(i), format="wav")
    print(i)