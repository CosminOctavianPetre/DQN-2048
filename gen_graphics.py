import sys
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter, NullFormatter


def make_graphs(csv_path, output_files=None):
    df = pd.read_csv(csv_path)
    
    episode = df['episode']
    max_tile = df['max_tile']
    episode_reward = df['episode_reward']
    episode_steps = df['episode_steps']

    num_episodes = len(episode)
    frequency_df = max_tile.value_counts().reset_index()
    frequency_df.columns = ['Max-Tile', 'Frequency']
        
    frequency_df = frequency_df.sort_values(by='Max-Tile')
    frequency_df['Max-Tile'] = frequency_df['Max-Tile'].astype(str)
    frequency_df['Frequency'] /= num_episodes
        
    # Max tile figure
    f1, ax1 = plt.subplots()
    f1.suptitle(r"$\bf{Baldosa\ máxima\ vs.\ Partidas\ Jugadas}$", fontsize=16)
    ax1.scatter(episode, max_tile, s=1)
    ax1.set_xlabel("Partida #")
    ax1.set_ylabel("Baldosa máxima alcanzada")
    ax1.set_yscale('log', base=2)
    ax1.yaxis.set_major_formatter(ScalarFormatter())
    ax1.yaxis.set_minor_formatter(NullFormatter())
    
    # Reward figure
    f2, ax2 = plt.subplots()
    f2.suptitle(r"$\bf{Puntuación\ vs.\ Partidas\ Jugadas}$", fontsize=16)
    ax2.scatter(episode, episode_reward, s=1)
    ax2.set_xlabel("Partida #")
    ax2.set_ylabel("Puntuación")
    
    # Max tile frequency figure
    f3, ax3 = plt.subplots()
    f3.suptitle(r"$\bf{Baldosa\ Máxima\ Alcanzada\ (Frecuencia)}$", fontsize=16)
    ax3.bar(frequency_df['Max-Tile'], frequency_df['Frequency'])
    ax3.set_xlabel("Baldosa máxima alcanzada")
    ax3.set_ylabel("Frecuencia (% partidas)")

    if output_files:
        f1.savefig(output_files[0])
        f2.savefig(output_files[1])
        f3.savefig(output_files[2])
    else:
        f1.show()
        f2.show()
        f3.show()


def main():
    csv_file = sys.argv[1]
    output_files = (csv_file[:-4]+'_fig1.png', csv_file[:-4]+'_fig2.png', csv_file[:-4]+'_fig3.png')

    make_graphs(csv_file, output_files)


if __name__ == "__main__":
    main()