import librosa
def getdata(file):
    
    y, sr = librosa.load(file)
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
    
    mfccs_vars = []
    for i in range(20):
        #mfccs_means.append(mfccs[i].mean())
        mfccs_vars.append(mfccs[i].var())

    data.append(chroma_stft_mean)
    data.append(chroma_stft_var)
    data.append(rms_mean)
    data.append(rms_var)
    data.append(spectral_centroid_mean)
    data.append(spectral_centroid_var)
    data.append(spectral_bandwidth_mean)
    data.append(spectral_bandwidth_var)
    data.append(rolloff_mean)
    data.append(rolloff_var)
    data.append(zero_crossing_rate_mean)
    data.append(zero_crossing_rate_var)
    data.append(harmony_mean)
    data.append(harmony_var)
    data.append(perceptr_mean)
    data.append(perceptr_var)
    data.append(tempo)
    for i in range(20):
        data.append(mfccs_vars[i])
        
    return data