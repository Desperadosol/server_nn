from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

INPUTS = 18
OUTPUTS = 16

def create_model(num_q: int, a, b, c, num_s: int):
    model = Sequential([
        Dense(a, activation='relu', input_shape=(num_q, )),  
        Dense(b, activation='relu'),
        Dense(c, activation='relu'),  
        Dense(num_s, activation='sigmoid')  
    ])
    # Compile the model
    model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

    return model

if __name__ == "__main__":
    model = create_model(INPUTS, 64, 64, 32, OUTPUTS)
    model.save('./model1.keras')

