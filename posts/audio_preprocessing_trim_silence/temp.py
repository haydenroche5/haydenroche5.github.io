fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(16, 12))

youtube_meow, sr = librosa.core.load('./data/meow/youtube_Q2WxLrS94RM_117.wav',
                                     sr=None)
num_samples = len(youtube_meow)
t = np.arange(num_samples)
axs[0][0].plot(t, youtube_meow)

t_ticks = np.linspace(0, num_samples, num=5)
t_tick_labels = ['{:.2f}'.format(t_tick / sr) for t_tick in t_ticks]
axs[0][0].set_xticks(t_ticks)
axs[0][0].set_xticklabels(t_tick_labels)

axs[0][0].set_xlabel('Time')
axs[0][0].set_ylabel('Amplitude')

axs[0][0].set_title('Meow 0 ')

####

top_db = 12
youtube_meow_trimmed = librosa.effects.trim(youtube_meow, top_db=top_db)[0]
num_samples_trimmed = len(youtube_meow_trimmed)
t_trimmed = np.arange(num_samples_trimmed)
axs[0][1].plot(t_trimmed, youtube_meow_trimmed)

t_ticks = np.linspace(0, num_samples_trimmed, num=5)
t_tick_labels = ['{:.2f}'.format(t_tick / sr) for t_tick in t_ticks]
axs[0][1].set_xticks(t_ticks)
axs[0][1].set_xticklabels(t_tick_labels)

axs[0][1].set_xlabel('Time')
axs[0][1].set_ylabel('Amplitude')

axs[0][1].set_title(f'Meow 0 Trimmed')

####

newton_meow, sr = librosa.core.load('./data/meow/newton_1.wav', sr=None)
num_samples = len(newton_meow)
t = np.arange(num_samples)
axs[1][0].plot(t, newton_meow)

t_ticks = np.linspace(0, num_samples, num=5)
t_tick_labels = ['{:.2f}'.format(t_tick / sr) for t_tick in t_ticks]
axs[1][0].set_xticks(t_ticks)
axs[1][0].set_xticklabels(t_tick_labels)

axs[1][0].set_xlabel('Time')
axs[1][0].set_ylabel('Amplitude')

axs[1][0].set_title('Newton Meow')

####

newton_meow_trimmed = librosa.effects.trim(newton_meow, top_db=top_db)[0]
num_samples_trimmed = len(newton_meow_trimmed)
t_trimmed = np.arange(num_samples_trimmed)
axs[1][1].plot(t_trimmed, newton_meow_trimmed)

t_ticks = np.linspace(0, num_samples_trimmed, num=5)
t_tick_labels = ['{:.2f}'.format(t_tick / sr) for t_tick in t_ticks]
axs[1][1].set_xticks(t_ticks)
axs[1][1].set_xticklabels(t_tick_labels)

axs[1][1].set_xlabel('Time')
axs[1][1].set_ylabel('Amplitude')

axs[1][1].set_title(f'Newton Example Trimmed')