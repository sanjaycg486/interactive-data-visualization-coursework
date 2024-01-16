# Interactive Data Visualization Course

This is the archive for my assignments to the Master Course [Interactive Data Visualization (SS 2020)](https://cs.uni-paderborn.de/en/cgvb/lehre/vergangene-semester/ss-20/interactive-data-visualization) by Prof. Dr. Gitta Domik-Kienegger at [Paderborn University](https://www.uni-paderborn.de/en/), Germany.

**Note:** The assignment sheets include proprietary material owned by Prof. Sabrina Piasecki, [Paderborn University](https://www.uni-paderborn.de/en/), Germany. And please don't share.

## Table of Contents

1. [Assignment 1](#assignment-1)
2. [Assignment 2](#assignment-2)
3. [Assignment 3](#assignment-3)
4. [Assignment 4](#assignment-4)
5. [Assignment 5](#assignment-5)
6. [How To Run](#how-to-run)
7. [License](#license)

## Assignment 1

**Task:** [Effective visual identification of quickest and slowest movements of water particles in a channel due to wind forces.](Assignment_1\ass1_sheet.pdf)

**Output:**

![Output for Assignment 1](Assignment_1\FlowData.png)

**Feedback:**
1. Points: 5/10.
2. Use of color is incorrect, false information is conveyed.
3. Flow direction is not clear cause of areas with too small arrows and areas with too much overlapping

## Assignment 2

Description of Assignment 2.

## Assignment 3

Description of Assignment 3.

## Assignment 4

Description of Assignment 4.

## Assignment 5

Description of Assignment 5.

## How to Run

This project uses Conda for managing environments and dependencies. The [`environment.yaml`](environment.yml) file contains the list of all dependencies needed to run the project.

Follow these steps to run the project:

1. **Install Conda**: If you haven't installed Conda yet, you can download it from [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html). Follow the instructions for your specific operating system.

2. **Create a Conda environment**: Navigate to the project directory in your terminal and run the following command to create a new Conda environment based on the [`environment.yaml`](environment.yml) file:

    ```bash
    conda env create -f environment.yaml
    ```

    This will create a new Conda environment with the name specified in the [`environment.yaml`](environment.yml) file.

3. **Activate the Conda environment**: Use the following command to activate the newly created environment:

    ```bash
    conda activate covid-19
    ```    

4. **Run the project**: Now that the environment is set up and activated, you can run the project. If it's a Python script, use the following command:

    ```bash
    python COVID-19.py
    ```    

Remember to deactivate the Conda environment once you're done by using the `conda deactivate` command.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details