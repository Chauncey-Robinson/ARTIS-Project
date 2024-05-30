# ARTIS Voice-Activated Assistant

## Project Overview

ARTIS (Astronaut Helmet Voice Assistant) is an innovative project aimed at enhancing operational safety and efficiency for astronauts through a sophisticated voice-activated assistant integrated into their helmets. This assistant leverages cutting-edge AI technologies to provide real-time data, proactive system checks, and emergency guidance, tailored to the unique challenges of space missions.

## Key Features

- **Voice Activation**: Utilizes the Vosk library for offline speech recognition to ensure functionality in environments with limited or no internet connectivity.
- **Real-Time Assistance**: Integrates with NASA APIs to provide astronauts with up-to-date information on space conditions, mission-critical data, and procedural guidelines.
- **Proactive Features**: Automatically checks the status of spacecraft systems based on specific triggers or commands and provides real-time updates and alerts.
- **Emergency Preparedness**: Offers critical information and step-by-step guidance during emergency scenarios such as sudden temperature drops, dust storms, or equipment failures.

## Technologies Used

- **Python**: Primary programming language for development.
- **Vosk**: For offline speech recognition.
- **Transformers (BERT, GPT)**: For advanced natural language understanding and dialogue management.
- **NASA APIs**: For real-time data integration.
- **Machine Learning**: Algorithms like random forests for predictive modeling.
- **Matplotlib**: For data visualization.
- **xarray and netCDF4**: For handling and analyzing environmental data.

## Project Structure

- **artis.py**: Contains the main functionalities and integrations for the ARTIS system.
- **artis_prototype.py**: Script for testing and prototyping the ARTIS assistant.
- **artis_space_data_fetch.py**: Script for fetching and processing space-related data from NASA APIs.

## Getting Started

### Prerequisites

- **Python 3.8+**
- **Virtual Environment**: Create a virtual environment to manage dependencies.
- **Required Libraries**: Install the required libraries using pip.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Chauncey-Robinson/ARTIS-Project.git
   cd ARTIS-Project
