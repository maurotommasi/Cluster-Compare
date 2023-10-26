import pandas as pd
import numpy as np

class CC:

    def __init__(self, _population, _target, _behaviors, _cc_name = 'ClusterCompare', _cc_key = 'ID', _cc_target_match = 'targetMatch'):
        if self.__safeInit(_population, _target, _behaviors, _cc_key):
            self.data = pd.merge(_population, _target, on=_cc_key, how='left')
            self.cc_key = _cc_key
            self.cc_target_match = _cc_target_match
            self.behaviors = _behaviors
            self.cc_name = _cc_name
            self.analysis = None
            self.compare_data = None
            print(f'Cluster Compare "{_cc_name}" Initialized')
            return None
        else:
            print('Cannot Initialize Cluster Compare')

    def __safeInit(self, _population, _target, _behaviors, _cc_key = 'ID'):
        # Check if __cc_krey is available in both dataframes
         return _cc_key in _population and _cc_key in _target and len(_behaviors) > 0
    
    def analyse(self):
        melted_df = pd.melt(self.data, id_vars=[self.cc_key, self.cc_target_match], value_vars=self.behaviors, var_name='Behavior', value_name='Value')
        filtered_df = melted_df[melted_df[self.cc_target_match] == 1]
        population_behavior_counts = melted_df.groupby(['Behavior', 'Value']).size().reset_index(name=f'Count Population {self.cc_name}')
        target_behavior_counts = filtered_df.groupby(['Behavior', 'Value']).size().reset_index(name=f'Count Target {self.cc_name}')
        self.analysis = pd.merge(population_behavior_counts, target_behavior_counts, on=['Behavior', 'Value'], how='left')
        self.analysis[f'Index T/P {self.cc_name}'] =  self.analysis[f'Count Target {self.cc_name}'] / self.analysis[f'Count Population {self.cc_name}']

    def getAnalysis(self):
        if self.analysis is not None:
            return self.cc_name, self.analysis
        else:
            print(f"Analysis not detected for CC {self.cc_name}")
            return None, None
    
    def compare(self, _cc_list_analysis):
        if self.analysis is not None:
            compare_df = self.analysis
            for cc_analysis in _cc_list_analysis:
                analysis_name, cc_analysis_data = cc_analysis
                compare_df = pd.merge(compare_df, cc_analysis_data, on=['Behavior', 'Value'], how='left')
                compare_df[f'Leverage {self.cc_name}/{analysis_name}'] = self.analysis[f'Index T/P {self.cc_name}'] / cc_analysis_data[f'Index T/P {analysis_name}']
            self.compare_data = compare_df
            return compare_df
        else:
            print(f"Analysis not detected for CC {self.cc_name}")
            return None, None
    
    def getFeatures(self, _thresholds):
        average_cols = [selected_col for selected_col in self.compare_data.columns if selected_col.startswith('Leverage')]
        condition = None

        # Iterate through thresholds and apply conditions
        for index in range(0, len(_thresholds)):
            threshold_condition = self.compare_data[average_cols[index]] > _thresholds[index]
            if condition is None:
                condition = threshold_condition
            else:
                condition = condition & threshold_condition

        filtered_data = self.compare_data[condition]

        return filtered_data

    def getDataset(self):
        return self.data
