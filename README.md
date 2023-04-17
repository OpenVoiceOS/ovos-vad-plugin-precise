# PreciseVAD

a VAD plugin trained with [precise-lite-trainer](https://github.com/OpenVoiceOS/precise-lite-trainer)

this initial version was trained on CommonVoice and some non-speech datasets I had available from training wake words.

a better dataset is being collected to train another model and will be documented

# Logs

some quick logs taken with ovos-dinkum-listener, threshold can be tuned for your microphone

a usb pseye mic was used for testing

with silence after the wake word, probability remains < 0.1
```
2023-04-17 19:27:23.680 - OVOS - __main__:_record_begin:283 - DEBUG - Record begin
2023-04-17 19:27:23.778 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.012165711194470092
2023-04-17 19:27:23.779 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.007387953200404283
2023-04-17 19:27:23.779 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.0074164837438903996
2023-04-17 19:27:23.916 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.00963889665079164
2023-04-17 19:27:24.075 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.0015273538706807768
2023-04-17 19:27:24.154 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.0013048631504227427
2023-04-17 19:27:24.312 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.004202510508154393
2023-04-17 19:27:24.392 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.011264940791642497
2023-04-17 19:27:24.551 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.029089080423976375
2023-04-17 19:27:24.709 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.0330160392731354
2023-04-17 19:27:24.789 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.04045075434080284
2023-04-17 19:27:24.940 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.035880844467858636
2023-04-17 19:27:25.098 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.0343127893222466
2023-04-17 19:27:25.177 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.048825275993444835
2023-04-17 19:27:25.336 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.06496073160893169
2023-04-17 19:27:25.415 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.06533937089905799
2023-04-17 19:27:25.574 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.020742919937412153
2023-04-17 19:27:25.733 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.03015348096774408
2023-04-17 19:27:25.812 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.03280407266906129
2023-04-17 19:27:25.970 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.033551127034316175
2023-04-17 19:27:26.050 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.02258507788816991
2023-04-17 19:27:26.208 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.021683746631835112
2023-04-17 19:27:26.367 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.014940036273039907
2023-04-17 19:27:26.441 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.023203975309233977
2023-04-17 19:27:26.599 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.010978107529107326
2023-04-17 19:27:26.758 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.01085717516984829
2023-04-17 19:27:26.838 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.00673192570027706
2023-04-17 19:27:26.996 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.009145248970350673
2023-04-17 19:27:27.075 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.014728564085050872
2023-04-17 19:27:27.234 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.018967839075865807
2023-04-17 19:27:27.393 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.021906081942161357
2023-04-17 19:27:27.472 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.020956804970967465
2023-04-17 19:27:27.631 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.0283355462028866
2023-04-17 19:27:27.710 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.03398455944396449
2023-04-17 19:27:27.868 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.04453903342935014
2023-04-17 19:27:28.021 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.04238703692519086
2023-04-17 19:27:28.099 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.04019838764322674
2023-04-17 19:27:28.259 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.02769013747752503
2023-04-17 19:27:28.419 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.01499332085241939
2023-04-17 19:27:28.497 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.006008901477572134
2023-04-17 19:27:28.655 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.0045410861370690616
2023-04-17 19:27:28.735 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.0027176982604409645
2023-04-17 19:27:28.894 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.003474307268425031
2023-04-17 19:27:29.052 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.0036373366435647186
2023-04-17 19:27:29.132 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.006373721983397192
2023-04-17 19:27:29.291 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.009820855380996639
2023-04-17 19:27:29.443 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.026175543470491943
2023-04-17 19:27:29.522 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.0203906866834103
2023-04-17 19:27:29.681 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.012525286747740462
2023-04-17 19:27:29.760 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.008839902469956445
2023-04-17 19:27:29.919 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.005125477038747509
2023-04-17 19:27:30.078 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.03135289363471317
2023-04-17 19:27:30.157 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.0501774431087121
2023-04-17 19:27:30.316 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.04399249493571764
2023-04-17 19:27:30.474 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.037273510113372876
2023-04-17 19:27:30.554 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.02796516340765478
2023-04-17 19:27:30.713 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.014262378958243262
2023-04-17 19:27:30.793 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.006917675543123764
2023-04-17 19:27:30.944 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.007190964077191803
2023-04-17 19:27:31.103 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.0031543336871801423
2023-04-17 19:27:31.182 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.004690789790075773
2023-04-17 19:27:31.341 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.0030493663030975084
2023-04-17 19:27:31.500 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.007445112471145236
2023-04-17 19:27:31.579 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.010005859629393689
2023-04-17 19:27:31.738 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.00699867247156005
2023-04-17 19:27:31.817 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.010897353990519618
2023-04-17 19:27:31.975 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.007736864654712764
2023-04-17 19:27:32.133 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.008414858717085034
2023-04-17 19:27:32.212 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.008974473819920836
2023-04-17 19:27:32.371 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.006449014494575834
2023-04-17 19:27:32.523 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.0062499767732257265
2023-04-17 19:27:32.602 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.006837515874981506
2023-04-17 19:27:32.760 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.0073311854962891726
2023-04-17 19:27:32.840 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.009283943655403859
2023-04-17 19:27:32.998 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.010737426081278957
2023-04-17 19:27:33.157 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.012570888528013672
2023-04-17 19:27:33.236 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.02473344466122114
2023-04-17 19:27:33.394 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.024982791734738385
2023-04-17 19:27:33.631 - OVOS - ovos_dinkum_listener.voice_loop.voice_loop:_after_cmd:431 - DEBUG - transformers metadata: {'client_name': 'ovos_dinkum_listener', 'source': 'audio', 'destination': ['skills']}
```

with speech after the wake word, during speech probability is between 0.5 and 0.99
```python
2023-04-17 19:27:36.716 - OVOS - __main__:_record_begin:283 - DEBUG - Record begin
2023-04-17 19:27:36.873 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.0074738396751538125
2023-04-17 19:27:36.874 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.005463857926285648
2023-04-17 19:27:36.874 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.0030883582006644853
2023-04-17 19:27:36.945 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.0037136731908849635
2023-04-17 19:27:37.104 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.004728898006598107
2023-04-17 19:27:37.184 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.0030493663030975084
2023-04-17 19:27:37.342 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.0031410389137608414
2023-04-17 19:27:37.502 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.025150235592824657
2023-04-17 19:27:37.580 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.023047880477860005
2023-04-17 19:27:37.739 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.03186467857525982
2023-04-17 19:27:37.897 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.02548805399370427
2023-04-17 19:27:37.976 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.01970189245134693
2023-04-17 19:27:38.134 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.016381035309930944
2023-04-17 19:27:38.213 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.019033565640216746
2023-04-17 19:27:38.372 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.014313525991548993
2023-04-17 19:27:38.526 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.01943213422131634
2023-04-17 19:27:38.605 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.013177221757724856
2023-04-17 19:27:38.763 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.01225473752907891
2023-04-17 19:27:38.922 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.026262602221521738
2023-04-17 19:27:39.001 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.027417460114405132
2023-04-17 19:27:39.160 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.05125093034399201
2023-04-17 19:27:39.239 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.0472147014568574
2023-04-17 19:27:39.398 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.11362504696008084
2023-04-17 19:27:39.557 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.5593268408157918
2023-04-17 19:27:39.636 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.7194453226817796
2023-04-17 19:27:39.795 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.8158054922282034
2023-04-17 19:27:39.874 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.8774687703063826
2023-04-17 19:27:40.027 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.9534068029700106
2023-04-17 19:27:40.186 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.5817289460986372
2023-04-17 19:27:40.264 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.799326634796633
2023-04-17 19:27:40.424 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.9263158586794051
2023-04-17 19:27:40.582 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.9649571924637619
2023-04-17 19:27:40.661 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.9905739379712881
2023-04-17 19:27:40.820 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.9645149239189981
2023-04-17 19:27:40.899 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.8768197419467589
2023-04-17 19:27:41.057 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.7557448514449752
2023-04-17 19:27:41.216 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.7123238196389171
2023-04-17 19:27:41.295 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.5744186314762657
2023-04-17 19:27:41.448 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.5140038699014324
2023-04-17 19:27:41.606 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.19568735916628419
2023-04-17 19:27:41.686 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.04007271005723843
2023-04-17 19:27:41.845 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.055409797254604584
2023-04-17 19:27:41.924 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.023439845868977315
2023-04-17 19:27:42.083 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.023360991166509474
2023-04-17 19:27:42.241 - OVOS - ovos_vad_plugin_precise:is_silence:19 - DEBUG - speech probability: 0.039947368706159704
2023-04-17 19:27:42.320 - OVOS - ovos_dinkum_listener.voice_loop.voice_loop:_after_cmd:431 - DEBUG - transformers metadata: {'client_name': 'ovos_dinkum_listener', 'source': 'audio', 'destination': ['skills']}
```