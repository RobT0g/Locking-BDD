# Locking-BDD
Locking system using BDD


# Setup
- Recommend using VSCode with the following extensions (everything is optional if you think about it):
    - Python
    - Cucumber
    - Cucumber (Gherkin) Full Support
    - Cucumber TsFlow for VS Code
    - Pytest BDD
    - MATLAB

- Create the python Virtual Environment by using the command `python -m venv .venv`
- Activate the environment with the command `.venv\Scripts\activate`
- Install all dependencies with the command `pip install -r reqs.txt`

To work with the simulink model you need to have Matlab (2023b or newer) installed. You need to install the Matlab engine for python to stablish communication, recommed following the tutorial [Install MATLAB Engine API for Python](https://www.mathworks.com/help/matlab/matlab_external/install-the-matlab-engine-for-python.html)
- As we are using a virtual environment here make sure to activate it before the installation process, this will ensure the project can use the library functions!!!

## Useful Links:
- [Matlab Code Generation Documentation](https://www.mathworks.com/help/overview/code-generation.html?s_tid=hc_panel)
- [Simulink Coder](https://www.mathworks.com/help/rtw/index.html?s_tid=hc_product_card)
- [Embedded Coder](https://www.mathworks.com/help/ecoder/index.html?s_tid=hc_product_card)