import numpy as np
import matplotlib.pyplot as plt
import random
import matplotlib.animation as animation


def numbers_generator():
    random_numbers = []
    for i in range(n_groups):
        random_numbers.append(random.randint(0, 9))
    print(random_numbers)
    return random_numbers


def average_calculation(random_numbers):
    numbers_sum = 0
    for number in random_numbers:
        numbers_sum += number
    return round(numbers_sum / len(random_numbers))


def count_numbers(numbers):
    counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for number in numbers:
        counts[number] += 1
    return counts


def live_roll(i):
    global rolled_times
    if rolled_times > 10000:
        return

    ax_rolls.clear()
    ax_average.clear()

    rolled_numbers = numbers_generator()
    counted_numbers = count_numbers(rolled_numbers)
    rects1 = ax_rolls.bar(index, counted_numbers, bar_width,
                          alpha=opacity, color='b',
                          label=f'{rolled_times}')

    ax_rolls.set_xlabel('Number')
    ax_rolls.set_ylabel('Amount')
    ax_rolls.set_title('Central theorem - number rolling')
    ax_rolls.set_xticks(index + bar_width / 2)
    ax_rolls.set_xticklabels((0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    ax_rolls.legend()

    rolled_average = average_calculation(rolled_numbers)
    times_rolled[rolled_average] += 1
    rects2 = ax_average.bar(index, times_rolled, bar_width,
                            alpha=opacity, color='b',
                            label=f'{rolled_times}')

    ax_average.set_xlabel('Average')
    ax_average.set_ylabel('Times rolled this average')
    ax_average.set_title('Central theorem - Average')
    ax_average.set_xticks(index + bar_width / 2)
    ax_average.set_xticklabels((0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    ax_average.legend()

    rolled_times += 1


times_rolled = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

n_groups = 10
rolled_times = 0

index = np.arange(n_groups)
bar_width = 0.45
opacity = 0.4

fig = plt.figure(1, figsize=(9, 5))
fig.canvas.toolbar.pack_forget()

ax_average = plt.subplot(121)
ax_rolls = plt.subplot(122)

ani1 = animation.FuncAnimation(fig, live_roll, interval=100)
plt.show()
