import tensorflow as tf
from pathlib import Path

from chicken_disease.entity.config_entity import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, 
                 config: ModelTrainerConfig,):
        """
        Initializes a ModelTrainer object.

        Args:
            config (ModelTrainerConfig): The configuration object containing parameters for the model trainer.
        """

        self.config = config
   
    def fetch_base_model(self):
        """
        Fetches the base model for training.

        This method loads the base model, specified in the configuration, using the provided parameters.
        The model is then saved to the specified path in the configuration.
        """

        self.model = tf.keras.applications.vgg16.VGG16(input_shape=self.config.params_image_size,
                                                       weights=self.config.params_weights,
                                                       include_top=self.config.params_include_top,)

        self.save_model(path=self.config.base_model_path, 
                        model=self.model,)
    
    @staticmethod
    def train_base_model(model, classes, freeze_all, freeze_till, learning_rate,):
        """
        Trains the base model.

        This method takes a base model, specified by the 'model' parameter, and performs training on it.
        The training can include freezing specific layers based on the provided parameters.
        The resulting trained model is compiled and returned.

        Args:
            model (tf.keras.Model): The base model to train.
            classes (int): The number of classes for classification.
            freeze_all (bool): Whether to freeze all layers of the model.
            freeze_till (int): Number of layers to freeze starting from the end. If None, no layers are frozen.
            learning_rate (float): The learning rate for the optimizer.

        Returns:
            tf.keras.Model: The trained model.
        """
        if freeze_all:
            for layer in model.layers:
                model.trainable = False

        elif (freeze_till is not None) and (freeze_till > 0):
            for layer in model.layers[:-freeze_till]:
                model.trainable = False

        flatten_in = tf.keras.layers.Flatten()(model.output)

        prediction = tf.keras.layers.Dense(units=classes,
                                           activation="softmax")(flatten_in)

        trained_model = tf.keras.models.Model(inputs=model.input,
                                           outputs=prediction)

        trained_model.compile(optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
                              loss=tf.keras.losses.CategoricalCrossentropy(),
                              metrics=["accuracy"])

        trained_model.summary()
        return trained_model    

    def base_model_trainer(self):
        """
        Trains the base model specified in the configuration.

        This method trains the base model by calling the 'train_base_model' method with the appropriate parameters.
        The resulting trained model is saved to the specified path in the configuration.
        """

        self.trained_model = self.train_base_model(model=self.model,
                                                   classes=self.config.params_classes,
                                                   freeze_all=True,
                                                   freeze_till=None,
                                                   learning_rate=self.config.params_learning_rate,)

        self.save_model(path=self.config.trained_model_path, 
                        model=self.trained_model,)
    
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        """
        Saves a Keras model to a specified path.

        Args:
            path (Path): The path to save the model.
            model (tf.keras.Model): The Keras model to save.
        """
        
        model.save(path)