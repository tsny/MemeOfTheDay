# Changelog

## [0.0.3] - Aug 10, 2018

### Changed

- main.py checks if it is being run as __main__

### Added

- More documentation comments

### Removed

- One line function for updating status

## [0.0.2] - Aug 8, 2018

### Changed

- memeoftheday.py -> main.py
- pathHelper.py -> setup.py

### Added

- First time setup if settings.json does not exist
- Verifies if settings.json is correct and credentials are correct
- Prints out username if login was successful
- -sp, --setup argument that recreates settings.json and gets twitter credentials from user input

## [0.0.1] - Aug 8, 2018
### Changed

- Changed file structure
- Improved README and CHANGELOG
- memeoftheday.py refactoring

### Added

- pathHelper.py handles file validation
- GNU License
- Login() and FindTodaysMeme() Documentation Comments

### Removed

- Unnecessary directories and C# project files
