# Sine Starter

![Frequency slider bound to fused.params driving a canvas sine plot](preview.png)

The smallest useful fused-app — a working example of the whole authoring
model in two files:

- `sine.py` — a plain Python `main(n, freq)` that returns points.
- `index.html` — a slider bound to `fused.params` (so state syncs to the
  URL) calling `fused.runPython("./sine.py", {freq})` and plotting the
  result on a canvas.

Drag the slider; refresh or bookmark the page and the exact state comes
back. Copy this folder and replace the two files to start your own app.

This remix is based on [vasu2001/sine-starter](https://github.com/vasu2001/sine-starter) by vasu2001, and we're grateful for their original work.
