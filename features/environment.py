from behave import *
import matlab.engine
import time


latency = 2

class ModelManager:
    def __init__(self, model_name:str):
        self.eng = matlab.engine.connect_matlab()
        self.model_name = model_name[:-4]
        self.name = self.eng.eval('base','model')
        self.start_time = time.time()

    def init_model(self):
        '''
        Initializes the Simulink model.
        '''

        self.eng.open_system(self.model_name, nargout=0)
        self.eng.set_param(self.model_name, "SimulationCommand", "start", nargout=0)

    def deinit_model(self):
        '''
        Deinitializes the Simulink model.
        '''

        self.eng.set_param(self.model_name, "SimulationCommand", "stop", nargout=0)

    def write_to_model(self, var_name:str, payload:int, model_name:str=None):
        '''
        Sends data to the Simulink model.
        Args:
            var_name (str): The name of the variable in the model.
            payload (int): The value to send to the model.
        '''

        if model_name is None:
            model_name = self.model_name
        
        # else: model_name = self.eng.eval('base', model_name)

        print(f"Sending {model_name}/{var_name} to model with value {payload} and type {type(payload)}")
        self.eng.write_to_model(f'{model_name}/{var_name}', payload, 'Value', nargout=0)

    def read_from_model(self, var_name:str, model_name:str=None) -> str:
        '''
        Retrieves data from the Simulink model.
        Args:
            var_name (str): The name of the variable in the model.
        Returns:
            str: The value of the variable in the model.
        '''

        if model_name is None:
            model_name = self.model_name
        
        # else: model_name = self.eng.eval('base', model_name)

        value = self.eng.read_from_model(f'{model_name}/{var_name}', nargout=1)
        print(f"Getting {model_name}/{var_name} from model with value {value} and type {type(value)}")
        return value

    def get_elapsed_time_ms(self) -> int:
        """
        Returns the time elapsed since the ModelManager was instantiated, in milliseconds.
        """

        elapsed_time = (time.time() - self.start_time) * 1000  # Convert seconds to milliseconds
        return int(elapsed_time)
    
    def update_model_time(self):
        """
        Updates the simulation time.
        """

        self.write_to_model('ClockVal', self.get_elapsed_time_ms())

    def reset_simulation_time(self):
        """
        Resets the simulation time.
        """

        self.start_time = time.time()
        self.write_to_model('ClockVal', 0)

    def reset_simulation(self):
        """
        Resets the simulation.
        """

        self.eng.set_param(self.model_name, "SimulationCommand", "stop", nargout=0)
        self.eng.set_param(self.model_name, "SimulationCommand", "start", nargout=0)

def before_all(context):
    """
    Initializes the simulation environment before all tests.
    """

    model_name = "feature_model.slx"
    print(f'> Testing model: {model_name}')

    context.model = ModelManager(model_name)
    context.model.init_model()

def before_scenario(context, scenario):
    '''
    Runs before each scenario
    '''

    print(f"Starting scenario: {scenario.name}")
    context.model.reset_simulation()
    context.model.reset_simulation_time()

def after_step(context, step):
    '''
    Runs after each step
    '''

    context.model.update_model_time()

def after_scenario(context, scenario):
    '''
    Runs after each scenario
    '''

    print(f"Scenario finished: {scenario.name}")

def after_all(context):
    '''
    Runs after all tests are completed
    '''

    print("All tests done!!!")

    context.model.deinit_model()

if __name__ == '__main__':
    pass
    #before_all()
