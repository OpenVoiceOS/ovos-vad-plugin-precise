import os
import random
import shutil

final_p = "/tmp/vad"
shutil.rmtree(final_p, ignore_errors=True)

speech_samples = []
noise_samples = []

audioset = "/home/miro/PycharmProjects/ovos-precise-auto-trainer/dataset_dl/audioset-processing/output"

audioset_ignore = ["female singing", "male singing", "child singing",
                   "conversation", "speech noise, speech babble"]
audioset_speech = ["speech", "narration, monologue"]

noises = [
             # pdsounds, kitchen, ESC50, FSDK50, UrbanSound8k, ww_community noises subset, audioset subset
             "/home/miro/PycharmProjects/ovos-precise-auto-trainer/dataset_dl/non-speech/"
         ] + [f"{audioset}/{f}" for f in os.listdir(audioset) if f not in audioset_ignore + audioset_speech]
speech = [
    "/home/miro/PycharmProjects/ovos-audio-classifier-gender/test",  # common_voice from kaggle + BVC
    "/home/miro/PycharmProjects/ovos-precise-auto-trainer/dataset_dl/wake-word/alexa__converted",  # kaggle wake word dataset
    "/home/miro/PycharmProjects/ovos-precise-auto-trainer/dataset_dl/wake-word/Khwarizmi_1.0s__converted",  # kaggle wake word dataset
    "/home/miro/PycharmProjects/ovos-precise-auto-trainer/dataset_dl/wake-word/NAR_dataset__converted",
    "/home/miro/PycharmProjects/ovos-precise-auto-trainer/dataset_dl/wake-word/speech_commands_v001__converted",
    "/home/miro/PycharmProjects/ovos-precise-auto-trainer/dataset_dl/wake-word/ovos-ww-community-dataset-master__converted/wake-words"  # kaggle wake word datasets
    "/home/miro/PycharmProjects/ovos-precise-auto-trainer/dataset_dl/wake-word/robin_data__converted",  # private dataset for wake words
] + [f"{audioset}/{f}" for f in os.listdir(audioset) if f in audioset_speech]
for dataset in speech:
    for root, folders, files in os.walk(dataset):
        for f in files:
            if not f.endswith(".wav"):
                continue
            speech_samples.append(f"{root}/{f}")
for dataset in noises:
    for root, folders, files in os.walk(dataset):
        for f in files:
            if not f.endswith(".wav"):
                continue
            noise_samples.append(f"{root}/{f}")

speech = list(set(speech_samples))
noise = list(set(noise_samples))
print(len(speech))
print(len(noise))

random.shuffle(speech)
random.shuffle(noise)

thresh = int(len(speech) * 0.6)
train_speech = speech[:thresh]
test_speech = speech[thresh:]

thresh = int(len(noise) * 0.6)
train_noise = noise[:thresh]
test_noise = noise[thresh:]

os.makedirs(f"{final_p}/wake-word", exist_ok=True)
os.makedirs(f"{final_p}/not-wake-word", exist_ok=True)
os.makedirs(f"{final_p}/test/wake-word", exist_ok=True)
os.makedirs(f"{final_p}/test/not-wake-word", exist_ok=True)

for f in train_noise:
    dst = f"{final_p}/not-wake-word/{f.split('/')[-1]}"
    try:
        os.symlink(f, dst)
    except FileExistsError:
        continue

for f in train_speech:
    dst = f"{final_p}/wake-word/{f.split('/')[-1]}"
    try:
        os.symlink(f, dst)
    except FileExistsError:
        continue

for f in test_noise:
    dst = f"{final_p}/test/not-wake-word/{f.split('/')[-1]}"
    try:
        os.symlink(f, dst)
    except FileExistsError:
        continue

for f in test_speech:
    dst = f"{final_p}/test/wake-word/{f.split('/')[-1]}"
    try:
        os.symlink(f, dst)
    except FileExistsError:
        continue
