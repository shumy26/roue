# roue: Routine Engine

**roue** is a configurable planner CLI tool that will schedule your activities for the week, based on your energy levels for each hour of the day (you can configure this).

## Features

- **Configurable energy levels** for weekdays and weekends via YAML
- **Automatic scheduling**: activities are matched to time blocks with the required energy
- **Tabular weekly output** using [tabulate](https://pypi.org/project/tabulate/)


## Installation

1. Clone this repository:
    ```sh
    git clone https://github.com/shumy26/roue.git
    cd roue
    ```

2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Edit `config.yaml` to set your day start times and energy levels.
2. Run the planner:
    ```sh
    python3 src/main.py
    ```
3. Follow the prompts to add or remove activities for each day.  
   - Format: `<activity-name>,<energy>,<duration>,[set-time]`
   - Example: `Coding,medium,03:00,20:30`
   - Energy must be one of: `low`, `medium`, `high`
   - Duration and set-time are in `HH:MM` format
   - Type `done` when finished with a day

4. Your weekly plan will be saved to `saved_plan.txt` in a readable table.

## Configuration

Edit `config.yaml` to set your preferred start times and energy levels for weekdays and weekends.

Example:
```yaml
day_start_weekday: "05:00"
day_start_weekend: "07:00"

energy_levels_weekday: 
  "05:00" : low
  "07:00" : medium
  "08:00" : high
  "13:00" : low
  "14:00" : medium
  "16:00" : high
  "19:00" : low

energy_levels_weekend:
  "07:00" : medium
  "08:00" : high
  "13:00" : low
  "14:00" : medium
  "16:00" : high
  "19:00" : low
```
## License

MIT License. See [LICENSE](LICENSE).

---

## Example Output:

```
╔═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╦═══════╗
║       ║ Sun   ║ Mon   ║ Tue   ║ Wed   ║ Thu   ║ Fri   ║ Sat   ║
╠═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╬═══════╣
║ 05h00 ║       ║       ║       ║       ║       ║       ║       ║
║ 05h30 ║       ║       ║       ║       ║       ║       ║       ║
║ 06h00 ║       ║       ║       ║       ║       ║       ║       ║
║ 06h30 ║       ║       ║       ║       ║       ║       ║       ║
║ 07h00 ║       ║Coffee ║Coffee ║Coffee ║Coffee ║Coffee ║       ║
║ 07h30 ║       ║Coffee ║Coffee ║Coffee ║Coffee ║Coffee ║       ║
║ 08h00 ║       ║Reading║Reading║Reading║Reading║Reading║       ║
║ 08h30 ║       ║Reading║Reading║Reading║Reading║Reading║       ║
║ 09h00 ║       ║Walk   ║Walk   ║Walk   ║Walk   ║Walk   ║       ║
║ 09h30 ║       ║Walk   ║Walk   ║Walk   ║Walk   ║Walk   ║       ║
║ 10h00 ║       ║Uni    ║Uni    ║Uni    ║Uni    ║Uni    ║       ║
║ 10h30 ║       ║Uni    ║Uni    ║Uni    ║Uni    ║Uni    ║       ║
║ 11h00 ║       ║Uni    ║Uni    ║Uni    ║Uni    ║Uni    ║       ║
║ 11h30 ║       ║Uni    ║Uni    ║Uni    ║Uni    ║Uni    ║       ║
║ 12h00 ║       ║Lunch  ║Lunch  ║Lunch  ║Lunch  ║Lunch  ║       ║
║ 12h30 ║       ║Lunch  ║Lunch  ║Lunch  ║Lunch  ║Lunch  ║       ║
║ 13h00 ║       ║Lunch  ║Lunch  ║Lunch  ║Lunch  ║Lunch  ║       ║
║ 13h30 ║       ║Lunch  ║Lunch  ║Lunch  ║Lunch  ║Lunch  ║       ║
║ 14h00 ║       ║Uni    ║Uni    ║Uni    ║Uni    ║Uni    ║       ║
║ 14h30 ║       ║Uni    ║Uni    ║Uni    ║Uni    ║Uni    ║       ║
║ 15h00 ║       ║Uni    ║Uni    ║Uni    ║Uni    ║Uni    ║       ║
║ 15h30 ║       ║Uni    ║Uni    ║Uni    ║Uni    ║Uni    ║       ║
║ 16h00 ║       ║Uni    ║Uni    ║Uni    ║Uni    ║Uni    ║       ║
║ 16h30 ║       ║Uni    ║Uni    ║Uni    ║Uni    ║Uni    ║       ║
║ 17h00 ║       ║Uni    ║Uni    ║Uni    ║Uni    ║Uni    ║       ║
║ 17h30 ║       ║Uni    ║Uni    ║Uni    ║Uni    ║Uni    ║       ║
║ 18h00 ║       ║       ║       ║       ║       ║       ║       ║
║ 18h30 ║       ║       ║       ║       ║       ║       ║       ║
║ 19h00 ║       ║       ║       ║       ║       ║       ║       ║
║ 19h30 ║       ║       ║       ║       ║       ║       ║       ║
║ 20h00 ║       ║       ║       ║       ║       ║       ║       ║
║ 20h30 ║       ║       ║       ║       ║       ║       ║       ║
║ 21h00 ║       ║       ║       ║       ║       ║       ║       ║
║ 21h30 ║       ║       ║       ║       ║       ║       ║       ║
║ 22h00 ║       ║       ║       ║       ║       ║       ║       ║
║ 22h30 ║       ║       ║       ║       ║       ║       ║       ║
║ 23h00 ║       ║       ║       ║       ║       ║       ║       ║
║ 23h30 ║       ║       ║       ║       ║       ║       ║       ║
╚═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╩═══════╝
```