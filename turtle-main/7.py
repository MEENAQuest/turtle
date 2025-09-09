'''
| Value       | Meaning                                                       |
| ----------- | ------------------------------------------------------------- |
| `0`         | **Fastest** speed (no animation, turtle just draws instantly) |
| `1`         | Slowest speed 🐌                                              |
| `2–9`       | Medium speeds                                                 |
| `10`        | Fastest visible speed 🚀                                      |
| `"fastest"` | same as `0`                                                   |
| `"fast"`    | fast but visible                                              |
| `"normal"`  | default speed                                                 |
| `"slow"`    | slower                                                        |
| `"slowest"` | very slow                                                     |
'''
import turtle
t = turtle.Turtle()

t.speed(1)       # Very slow
t.forward(100)

t.speed(10)      # Very fast
t.right(90)
t.forward(100)

t.speed(0)       # Instant
t.circle(50)
turtle.done()