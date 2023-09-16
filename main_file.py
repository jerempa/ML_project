import data_processing
import data_visualization
import ml_model_implementation

def main():
    df = data_processing.main()

    #data_visualization.line_chart(df)
    ml_model_implementation.feature_matrix_and_target_vector(df)


main()