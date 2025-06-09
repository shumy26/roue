# roue: Routine Engine

**roue** is a configurable planner CLI tool that will schedule your activities for the week, based on your energy levels for each hour of the day (you can configure this).


Roue is a command-line tool for planning your week based on your energy levels. You define your daily energy patterns and add activities, and Roue helps you schedule them into your week, ensuring you match the right activity to the right energy slot.


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