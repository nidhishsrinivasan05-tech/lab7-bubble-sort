"""
Lab 7 - Bubble Sort Visualization

This project provides a Tkinter-based visualization of the Bubble Sort algorithm.
It also includes a console fallback and a self-test mode so the program can still
run in environments without a graphical display.

Run:
    python main.py

Optional:
    python main.py --console
    python main.py --matplotlib
    python main.py --test
"""

from __future__ import annotations

import random
import sys
import time
from typing import List


DEFAULT_BAR_COUNT = 30
MIN_VALUE = 10
MAX_VALUE = 100
DEFAULT_DELAY_MS = 80


def generate_data(size: int = DEFAULT_BAR_COUNT) -> List[int]:
    """Generate a random list of integers for sorting."""
    return [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(size)]


def bubble_sort_steps(data: List[int]):
    """
    Yield intermediate states of bubble sort.

    Yields tuples:
        (current_data, index_a, index_b, sorted_start)

    where:
        - current_data is a snapshot of the list
        - index_a and index_b are the compared indices
        - sorted_start marks the boundary of the sorted suffix
    """
    arr = data[:]
    n = len(arr)

    if n <= 1:
        yield arr[:], None, None, 0
        return

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            yield arr[:], j, j + 1, n - i
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                yield arr[:], j, j + 1, n - i
        if not swapped:
            break

    yield arr[:], None, None, 0


def run_console_visualization(data: List[int], delay: float = 0.08) -> List[int]:
    """Simple terminal visualization for environments without GUI support."""
    print("Bubble Sort Visualization (Console Mode)")
    print("Initial data:", data)
    final_state = data[:]

    for state, a, b, sorted_start in bubble_sort_steps(data):
        final_state = state[:]
        pieces = []
        for idx, value in enumerate(state):
            token = f"{value:02d}"
            if idx == a or idx == b:
                token = f"[{token}]"
            elif sorted_start and idx >= sorted_start:
                token = f"({token})"
            pieces.append(token)
        print(" ".join(pieces))
        time.sleep(delay)

    print("Sorted data:", final_state)
    return final_state


def run_matplotlib_visualization(
    data: List[int], interval_ms: int = DEFAULT_DELAY_MS
) -> List[int]:
    """Visualize bubble sort using Matplotlib animation."""
    try:
        import matplotlib.pyplot as plt
        from matplotlib.animation import FuncAnimation
    except Exception as exc:
        raise RuntimeError(
            "Matplotlib is unavailable. " "Install it with: pip install matplotlib"
        ) from exc

    steps = list(bubble_sort_steps(data))
    if not steps:
        return data[:]

    fig, ax = plt.subplots(figsize=(11, 5.5))
    x_positions = list(range(len(data)))
    bars = ax.bar(x_positions, data, color="#6fa8dc")
    ax.set_title("Bubble Sort Visualization (Matplotlib)")
    ax.set_xlabel("Index")
    ax.set_ylabel("Value")
    ax.set_xlim(-0.5, len(data) - 0.5)
    ax.set_ylim(0, max(data) * 1.2)

    status_text = ax.text(0.01, 0.97, "", transform=ax.transAxes, va="top")

    def update(frame_index: int):
        state, active_a, active_b, sorted_start = steps[frame_index]
        for idx, (bar, value) in enumerate(zip(bars, state)):
            bar.set_height(value)
            color = "#6aa84f" if sorted_start and idx >= sorted_start else "#6fa8dc"
            if idx in (active_a, active_b):
                color = "#e69138"
            bar.set_color(color)

        status_text.set_text(f"Step {frame_index + 1}/{len(steps)}")
        return list(bars) + [status_text]

    animation = FuncAnimation(
        fig,
        update,
        frames=len(steps),
        interval=interval_ms,
        repeat=False,
        blit=False,
    )

    plt.tight_layout()
    plt.show()

    final_state = steps[-1][0][:]
    print("Sorted data:", final_state)
    return final_state


def launch_gui(data: List[int]) -> None:
    """Launch the Tkinter visualization."""
    import tkinter as tk

    class BubbleSortApp:
        def __init__(self, root: tk.Tk, initial_data: List[int]) -> None:
            self.root = root
            self.root.title("Bubble Sort Visualization")
            self.root.geometry("1000x620")
            self.root.minsize(900, 540)

            self.data = initial_data[:]
            self.original_data = initial_data[:]
            self.step_generator = None
            self.is_running = False
            self.delay_ms = DEFAULT_DELAY_MS

            self.title_label = tk.Label(
                root,
                text="Bubble Sort Visualization",
                font=("Arial", 22, "bold"),
                pady=10,
            )
            self.title_label.pack()

            controls = tk.Frame(root, pady=5)
            controls.pack()

            tk.Button(
                controls, text="Generate New Data", command=self.reset_data, width=16
            ).grid(row=0, column=0, padx=5)
            tk.Button(
                controls, text="Start Sorting", command=self.start_sorting, width=16
            ).grid(row=0, column=1, padx=5)
            tk.Button(
                controls, text="Shuffle", command=self.shuffle_data, width=12
            ).grid(row=0, column=2, padx=5)

            tk.Label(controls, text="Bars:").grid(row=0, column=3, padx=(15, 5))
            self.size_scale = tk.Scale(
                controls, from_=10, to=60, orient="horizontal", length=180
            )
            self.size_scale.set(len(self.data))
            self.size_scale.grid(row=0, column=4, padx=5)

            tk.Label(controls, text="Speed (ms):").grid(row=0, column=5, padx=(15, 5))
            self.speed_scale = tk.Scale(
                controls, from_=10, to=500, orient="horizontal", length=180
            )
            self.speed_scale.set(self.delay_ms)
            self.speed_scale.grid(row=0, column=6, padx=5)

            self.status_var = tk.StringVar(
                value="Ready. Press 'Start Sorting' to begin."
            )
            tk.Label(root, textvariable=self.status_var, font=("Arial", 11)).pack(
                pady=(0, 5)
            )

            self.canvas = tk.Canvas(root, width=960, height=440, bg="white")
            self.canvas.pack(padx=20, pady=10, fill="both", expand=True)

            self.draw_data(self.data)

        def shuffle_data(self) -> None:
            if self.is_running:
                return
            random.shuffle(self.data)
            self.original_data = self.data[:]
            self.status_var.set("Data shuffled.")
            self.draw_data(self.data)

        def reset_data(self) -> None:
            if self.is_running:
                return
            size = self.size_scale.get()
            self.data = generate_data(size)
            self.original_data = self.data[:]
            self.status_var.set("Generated new random data.")
            self.draw_data(self.data)

        def draw_data(
            self, data: List[int], active_a=None, active_b=None, sorted_start=0
        ) -> None:
            self.canvas.delete("all")

            canvas_width = max(self.canvas.winfo_width(), 960)
            canvas_height = max(self.canvas.winfo_height(), 440)

            if not data:
                return

            bar_width = canvas_width / len(data)
            max_value = max(data)

            for i, value in enumerate(data):
                x0 = i * bar_width + 4
                y0 = canvas_height - (value / max_value) * (canvas_height - 40)
                x1 = (i + 1) * bar_width - 4
                y1 = canvas_height - 10

                color = "#6aa84f" if sorted_start and i >= sorted_start else "#6fa8dc"
                if i == active_a or i == active_b:
                    color = "#e69138"

                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="")
                self.canvas.create_text(
                    (x0 + x1) / 2, y0 - 8, text=str(value), font=("Arial", 9)
                )

        def start_sorting(self) -> None:
            if self.is_running:
                return
            self.is_running = True
            self.delay_ms = self.speed_scale.get()
            self.step_generator = bubble_sort_steps(self.data)
            self.status_var.set("Sorting in progress...")
            self.run_next_step()

        def run_next_step(self) -> None:
            try:
                state, a, b, sorted_start = next(self.step_generator)
                self.data = state[:]
                self.draw_data(self.data, a, b, sorted_start)
                self.root.after(self.delay_ms, self.run_next_step)
            except StopIteration:
                self.is_running = False
                self.status_var.set("Sorting complete.")
                self.draw_data(self.data)

    root = tk.Tk()
    app = BubbleSortApp(root, data)
    root.mainloop()


def self_test() -> None:
    """Run a basic correctness check."""
    sample = [5, 1, 4, 2, 8]
    final_state = None
    for state, _, _, _ in bubble_sort_steps(sample):
        final_state = state
    assert final_state == sorted(
        sample
    ), f"Expected {sorted(sample)}, got {final_state}"
    print("Self-test passed. Final sorted state:", final_state)


def main() -> None:
    args = set(sys.argv[1:])

    if "--test" in args:
        self_test()
        return

    data = generate_data()

    if "--console" in args:
        run_console_visualization(data)
        return

    if "--matplotlib" in args:
        run_matplotlib_visualization(data)
        return

    try:
        launch_gui(data)
    except Exception as exc:
        print("GUI mode unavailable. Falling back to console mode.")
        print(f"Reason: {exc}")
        run_console_visualization(data, delay=0.03)


if __name__ == "__main__":
    main()
