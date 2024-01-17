# San International Airlines | Flight Announcement

## Overview
This Script has been made by TomBad to help Flight Director+ announce incoming Flights! 

## Installation
1. Make sure `git` and `Python` are installed on your Computer:

   [Install GIT](https:/git-scm.com/downloads) + [Install Python](https://www.python.org/downloads/)
2. Clone the repository:

    ```bash
    git clone https://github.com/TomBad13/SAL-Flight-Announcement.git
    ```
3. Navigate to the project directory:

    ```bash
    cd keep-talking-game
    ```
4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
5. Execute the Script with the Command under the `Usage` section.
   
## Usage
To use the Application, please use the following command after following the Installation Instructions.

```bash
python main.py [NUMBER] [AUTOMATIC CALLSIGNS] [SAME DATE] [DATE]
```
Replace `[NUMBER]` with the desired number of Flights you want to announce.

Replace `[AUTOMATIC CALLSIGNS]` with:
- `Y` to automatically choose the Next Callsign.
- `N` to manually choose every Callsign.

Replace `[SAME DATE]` with:
- `Y` to choose the same date for every Flight.
- `N` to manually choose the date for every Flight.

Replace `[DATE]` with the Date under the format DD/MM for every Flight, you can leave it blank if you chose `N` for "Same Date".

### Usage Recommandation
I recommend you use it like below to have a better automation of everything:
```bash
python main.py [NUMBER] Y Y [DATE]
```
