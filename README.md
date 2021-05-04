# HerbLens
## Indian herb recognition and Information retrieval.

There are variety of plants that occur in nature and are useful in many ways such as in drug formulation , production of herbal products, and medicines to cure many deseases.
India has rich amount of such medicinal plants. 

## Dataset and Goal/problem statement :
The dataset used in this project https://data.mendeley.com/datasets/nnytj2v3n5/1 contains leaf images of 30 categories of such Indian medicinal plants/herbs , such as Tulsi, Sandalwood , mint, neem and many more. The dataset contains 1835 images , with folder names as labels of the herbs, see the folder structure of the dataset given below.

The goal was to build an application which can identify/recognize the herb and display its scientific or botanical information and its medicinal properties and uses.
The contribution of the medicinal plant leaf dataset to develop Artificial Intelligence models (machine learning and deep learning) will assist many researchers and computer scientists to detect, identify the species and its diseases and learn more about the herb existence and medicinal properties.

Data </br>
|__ Herb_1 </br>
|  |__ Img_1 </br>
|  |__ Img_2 </br>
|  ... </br>
| </br>
|__ Herb_2 </br>
|  |__ Img_1 </br>
|  |__ Img_2 </br>
|  ... </br>
| </br>
... </br>
... </br>
| </br>
|__ Herb_30 </br>
|   |__ Img_1 </br>
|   |__ Img_2 </br>
|   ... </br>

var routes = (
  <Route name="Data">
    <Route name="Herb 1"/>
      <Route name="Image 1"/>
      <Route name="Image 2"/>
      <Route name="..."/>
  </Route>
  
  <Route name="Herb 2"/>
      <Route name="Image 1"/>
      <Route name="Image 2"/>
      <Route name="..."/>
  </Route>
 </Route>
  

);

## Approches :
There are many approches to solve this problem,and few of them are studied and implemented in Herblens.
Developing deep learning models using different learning algorithms such as :

1 ) Traditional convolutional neural networks
2 ) Transfer Learning Models
3 ) Few shot and one shot Learning Algorithms such as siamese and prototypical networks.

## Implementation :

### Tradistional CNN :
Build the cnn model by apply hyperparameter optimization :
Here's the notebook : https://github.com/E-DBDA/Project/blob/main/cnn_hypertuning_uzma.ipynb

### Transfer Learning Models :
#### Xception Model :
Xception by Google, stands for Extreme version of Inception. With a modified depthwise separable convolution, it is even better than Inception-v3  (also by Google, 1st Runner Up in ILSVRC 2015) for both ImageNet ILSVRC and JFT datasets.

Here's the motebook of Xception model : https://github.com/E-DBDA/Project/blob/main/Xception_uzma.ipynb
5-fold cv on Xception model : https://github.com/E-DBDA/Project/blob/main/5Fold_cv_on_Xception_uzma.ipynb

To know more about Xception model check this article : https://maelfabien.github.io/deeplearning/xception/

### One shot Learning Using siamese network :

Whereas most machine learning based object categorization algorithms require training on hundreds or thousands of samples/images and very large datasets, one-shot learning aims to learn information about object categories from one, or only a few, training samples/images.
To sample out single image of all the categories for training data the entropy sampling technique used where the image with highest entropy is taken.
Code for extracting best image from the data using entropy method : https://github.com/E-DBDA/Project/blob/main/best_image_extractor_for_one_shot_uzma.ipynb

Siamese Network : 
Siamese networks are a special type of neural network architecture. Instead of a model learning to classify its inputs, the neural networks learns to differentiate between two inputs. It learns the similarity between them.

The architecture
A Siamese networks consists of two identical neural networks(cnn), each taking one of the two input images. The last layers of the two networks gives the vector encoding of two images and then used the euclidean distance function , which calculates the similarity between the two images.The architecture is given below.


https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pyimagesearch.com%2F2020%2F11%2F30%2Fsiamese-networks-with-keras-tensorflow-and-deep-learning%2F&psig=AOvVaw37LTlEFzXRpQ8Y-TNOq7Zg&ust=1620194147858000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCPi46turr_ACFQAAAAAdAAAAABAD

There are two sister networks, which are identical neural networks, with the exact same weights.

Each image in the image pair is fed to one of these networks.

The code/notebook :
https://github.com/E-DBDA/Project/blob/main/one_shot_siamese_uzma.ipynb


## The HerbLens Application :
## Web UI using flask:
![image](https://user-images.githubusercontent.com/73434008/116971979-0020e000-acd8-11eb-9ed9-c881265b15cd.png)
![image](https://user-images.githubusercontent.com/73434008/116972196-4a09c600-acd8-11eb-87ea-d4b0b4cfa936.png)

## Android app UI :
![image](https://user-images.githubusercontent.com/73434008/116972501-b84e8880-acd8-11eb-8d15-793d15c616ad.png)



### All notebooks of the project build by all of the team members :
https://github.com/E-DBDA/Project






  



