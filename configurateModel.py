from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

INPUTS = 18
OUTPUTS = 16

def create_model(num_q: int, layers: list, num_s: int):
    model = Sequential([
        Dense(layers[0], activation='relu', input_shape=(num_q, )),  
        Dense(layers[1], activation='relu'),
        Dense(layers[2], activation='relu'),  
        Dense(num_s, activation='sigmoid')  
    ])
    # Compile the model
    model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

    return model

if __name__ == "__main__":
    model = create_model(INPUTS,[64,64,32],OUTPUTS)
    model.save('./model1.keras')

