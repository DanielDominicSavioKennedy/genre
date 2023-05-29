import librosa

y, sr = librosa.load(f'blues.00000.wav')

data=list()

chroma_stft_mean = librosa.feature.chroma_stft(y=y, sr=sr).mean()
chroma_stft_var = librosa.feature.chroma_stft(y=y, sr=sr).var()
rms_mean = librosa.feature.rms(y=y).mean()
rms_var = librosa.feature.rms(y=y).var()
spectral_centroid_mean = librosa.feature.spectral_centroid(y=y, sr=sr).mean()
spectral_centroid_var = librosa.feature.spectral_centroid(y=y, sr=sr).var()
spectral_bandwidth_mean = librosa.feature.spectral_bandwidth(y=y, sr=sr).mean()
spectral_bandwidth_var = librosa.feature.spectral_bandwidth(y=y, sr=sr).var()
rolloff_mean = librosa.feature.spectral_rolloff(y=y, sr=sr).mean()
rolloff_var = librosa.feature.spectral_rolloff(y=y, sr=sr).var()
zero_crossing_rate_mean = librosa.feature.zero_crossing_rate(y).mean()
zero_crossing_rate_var = librosa.feature.zero_crossing_rate(y).var()
harmony_mean = librosa.effects.harmonic(y=y).mean()
harmony_var = librosa.effects.harmonic(y=y).var()
perceptr_mean = librosa.effects.percussive(y=y).mean()
perceptr_var = librosa.effects.percussive(y=y).var()

tempo, _ = librosa.beat.beat_track(y=y, sr=sr)

mfccs = librosa.feature.mfcc(y=y, sr=sr)
mfccs_means = []
mfccs_vars = []
for i in range(20):
    #mfccs_means.append(mfccs[i].mean())
    mfccs_vars.append(mfccs[i].var())

print("chroma_stft_mean:", chroma_stft_mean)#1
data.append(chroma_stft_mean)
print("chroma_stft_var:", chroma_stft_var)#2
data.append(chroma_stft_var)
print("rms_mean:", rms_mean)#3
data.append(rms_mean)
print("rms_var:", rms_var)#4
data.append(rms_var)
print("spectral_centroid_mean:", spectral_centroid_mean)#5
data.append(spectral_centroid_mean)
print("spectral_centroid_var:", spectral_centroid_var)#6
data.append(spectral_centroid_var)
print("spectral_bandwidth_mean:", spectral_bandwidth_mean)#7
data.append(spectral_bandwidth_mean)
print("spectral_bandwidth_var:", spectral_bandwidth_var)#8
data.append(spectral_bandwidth_var)
print("rolloff_mean:", rolloff_mean)#9
data.append(rolloff_mean)
print("rolloff_var:", rolloff_var)#10
data.append(rolloff_var)
print("zero_crossing_rate_mean:", zero_crossing_rate_mean)#11
data.append(zero_crossing_rate_mean)
print("zero_crossing_rate_var:", zero_crossing_rate_var)#12
data.append(zero_crossing_rate_var)
print("harmony_mean:", harmony_mean)#13
data.append(harmony_mean)
print("harmony_var:", harmony_var)#14
data.append(harmony_var)
print("perceptr_mean:", perceptr_mean)#15
data.append(perceptr_mean)
print("perceptr_var:", perceptr_var)#16
data.append(perceptr_var)
print("tempo:", tempo)#17
data.append(tempo)

for i in range(20):
    #print(f"mfcc{i+1}_mean: {mfccs_means[i]}")
    print(f"mfcc{i+1}_var: {mfccs_vars[i]}")
    data.append(mfccs_vars[i])
    
print(data)
print(len(data))