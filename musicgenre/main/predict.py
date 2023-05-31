import pickle
import os

def predict_genre(meta1):
  
    #pickle_file_path = './mlmodel.p'
    #pickle_file_path = '../musicgenre/mlmodel.p'#os.path.join(os.getcwd(), 'mlmodel.p')
    from django.conf import settings
    pickle_file_path = os.path.join(settings.MODELS, 'mlmodel.p')

    # Load the pickle file
    with open(pickle_file_path, 'rb') as f:
        data = pickle.load(f)
    scaler = data['scaler']
    knn = data['knn']
    encoder = data['encoder']
    x = scaler.transform([meta1])
    pred = knn.predict(x)
    return(encoder.inverse_transform([pred]))

#print(predict_genre([0.3501285, 0.08877166, 0.13018432, 0.00282838, 1784.1226409867395, 129745.48453872248, 2002.4124070990924, 85834.4103621946, 3805.7230301080335, 901252.916706492, 0.08304482066898686, 0.0007669456545940504, -4.90663e-05, 0.008172463, -1.0618483e-05, 0.005704438, 123.046875, 2569.3694, 295.8471, 235.58444, 151.03874, 167.99287, 89.17242, 67.60309, 69.001495, 82.21984, 63.346542, 61.76499, 51.280754, 41.215897, 40.51752, 49.784233, 52.424534, 36.535866, 41.60317, 55.053654, 46.941353]))