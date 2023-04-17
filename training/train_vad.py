from precise_trainer import PreciseTrainer

model_name = "vad"
folder = f"/tmp/{model_name}"  # dataset here
model_path = f"~/PycharmProjects/ovos-audio-classifiers/trained/{model_name}"  # save here
log_dir = f"/tmp/logs/fit/{model_name}"  # for tensorboard

trainer = PreciseTrainer(model_path, folder, epochs=1000, log_dir=log_dir)
# trainer.augment_data()
model_file = trainer.train()
trainer.test()
