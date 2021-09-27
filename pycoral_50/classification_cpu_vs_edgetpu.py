import os
import subprocess
import pandas as pd


def classification_tests(base_dir, images_dir):
    rows = []
    models = [model for model in os.listdir(base_dir) if model.endswith('.tflite')]
    images_dirs = os.listdir(images_dir)
    for dir in images_dirs:
        images = os.listdir(os.path.join(images_dir, dir))
        for image in images[:10]:
            print(dir, image)
            for model in models:
                model_path = os.path.join(base_dir, model)
                cmd = f'''python3 classify_image.py \
                  --model {model_path}\
                  --labels {os.path.join(labels_dir, 'labels.txt')}\
                  --input {os.path.join(images_dir, dir, image)}\
                  --count 1 --top_k 4'''
                proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, )
                output = proc.communicate()[0].decode('utf-8')
                lines = output.split('\n')
                for line in lines[3:]:
                    if line != '':
                        rows.append([model, line.split(':')[0], line.split(':')[1]])

    df = pd.DataFrame(rows, columns=['model', 'inferecne', 'results'])
    df.to_csv(os.path.join(base_dir, f'comaparision_results.csv'), index=False)
    print(df)

    return df


base_dir = os.path.dirname(os.path.abspath(__file__))
model_dir = os.path.join(base_dir, 'models')
labels_dir = os.path.join(base_dir)
images_dir = os.path.join(base_dir, 'dataset')
classification_df = classification_tests(base_dir, images_dir)


