# Informal Literature Review of 3D Convolutional Networks
Updated: 09/25/17

#### OctNet: Learning Deep 3D Representations at High Resolutions:
  * Andreas Geiger, November 2016
  - Quote: Using our OctNet, we investigate the impact of high resolution in- puts wrt.
  accuracy on the three tasks and demonstrate that higher resolutions are
  particularly beneficial for orientation estimation and semantic point cloud
  labeling. (128^3 and above)

#### Large-Scale Shape Retrieval with Sparse 3D Convolutional Neural Networks:
  * Evgeny Burnaev, July 2017
  - Quote: Adding a third spatial dimension in the input grid correspondingly increases
   computational costs. Num- ber of cells scales as a power of three w.r.t. the
   resolution of the voxel grid. Low resolution grids make it difficult to
   differentiate between similar shapes, and lose some of the fine details
   available in 2D renderings of equivalent resolution.
   - Quote: Computational complexity of 3D convolution for image with dimensions of
   N × M × K with filters sizes of n × m × k is equal to O(NMKnmk)
   - ModelNet40, 0.0301 sec/sample on Titan X 12Gb, 90.30 % accuracy, 60-70 dim

#### Beam Search for Learning a Deep Convolutional Neural Network of 3D Shapes:
  * Sinisa Todorovic, December 2016
  - Layer 1: 16x6x6x6 stride 2, 64x5x5x5 stride 2, 64x5x5x5 stride 2, number of classes.
  - 81.26% accuracy on ModelNet 40, 30 dim, 5 hours training time.

#### Learning Efficient Point Cloud Generation for Dense 3D Object Reconstruction:
  * Simon Lucey, May 2017
  - Quote: Despite their recent success, 3D ConvNets suffer from an inherent drawback when
    modeling shapes with volumetric representations. Unlike 2D images, where every
    pixel contains meaningful spatial and texture information, volumetric
    representations are information-sparse. More specifically, a 3D object is
    expressed as a voxel-wise occupancy grid, where voxels “outside” the object
    (set to off) and “inside” the object (set to on) are unimportant and
    fundamentally not of particular interest. In other words, the richest information
    of shape representations lies on the surface of the 3D object, which makes up only
    a slight fraction of all voxels in an occupancy grid. Consequently, 3D ConvNets
    are extremely wasteful in both computation and memory in trying to predict much
    unuseful data with high-complexity 3D convolutions, severely limiting the
    granularity of the 3D volumetric shapes that can be modeled even on high-end
    GPU-nodes commonly used in deep learning research.

#### Generalized Convolutional Neural Networks for Point Cloud Data:
  * Aleksandr Savchenkov, JULY 2017
  - However,if the level of detail remains the same, and the scale of the problem
  grows (classifying a cloud as a sedan vs finding a sedan in a scene), sparsity
  grows. There is also the issue that the level of detail in real world scans
  varies across the image due to varying distances from the sensor. This requires
  that conventional convolutions work with smaller blocks as the unit volumes,
  increasing sparsity further. Applying a conventional convolution sparsely to
  combat this fact is challenging because convolution has a dilatory effect on
  tensors, where sparse tensors quickly become dense after very few convolutions.
  This means that when converting point clouds into occupation grids, one needs
  to keep sparsity, and thus resolution, low to maintain an input of reasonable
  size, losing information in the process.

#### ModelNet40 Top Voxel Networks:
  - VRN-Ensemble, 95.54%
  - VRN, 91.33%
  - FusionNet, 90.8%
  - Voxception, 90.56%
  - LightNet, 86.90%
  - VoxNet, 83%
  - Beam Searching, 81.26%
  - 3DShapeNets, 77%