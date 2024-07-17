# Project
This project is done in conenction with the Jetson AI Fundamentals course, https://developer.nvidia.com/embedded/learn/jetson-ai-certification-programs#course\_outline.

The aim of the project is to train a model that can predict - given a satellite image of agricultural areas - whether the image is a reservoir, reservoir with a dead spot
or a reservoir without a dead spot. The value of detecting water harvests autonomously (water extracted from rivers to private reservoirs) can significantly enhance water authorities' capabilities to detect potential illegal water harvesting activty in remote regions.   

## Why detecting water harvesting is important to society
Disruption to climate is causing agriculture to turn to irrigation as a safeguard for unreliable rainfall. As competition for freshwater increases, more farms are building private water storages to protect its ability to irrigate crops if a river periodically runs dry. When multiple farms creates water storages, evaporation increases - reducing both local water availability and productivity within a region. Such phenonema is known as "tragedy of the commons" and is decribed in environmental economics as an open-access and finite resource which generates value to consumers but is difficult to regulate to to its open areas. 
Such behaviour is known as water harvesting - the choice to build out dam-like infrastructure to pump water into the a privately held reservoir where no other agent can access it.  

## Satellite images and AI to track down floodplain harvesting activity
We approached the problem of water harvesting as an authority-stakeholder-idenfication problem, on par with illigal fishery. 
Similar to fishing, imagine you catch fish, and you see your neighboring vessel using equipment (or enters forbidden zones) in order to create a larger catch. 
You have a feeling something is wrong, yet, you cannot quantify the catch and you do not have legitimate evidence that something illegal is taking place. 

The same occurs when you grow crops through irrigation, and you see your neighbor having large pumps and stores water somewhere on private property. Now, as satellites are crossing the skies, it becomes possible to gather information. Though, detecting water harvesting is not as simple as detecting a can of Coca-Cola as water storages have various sizes and forms.   

## Creating two labels and assumptions for floodplain harvesting
To really get the model to understand what it is looking at - we must first understand it ourselves. As this [the behaviouar to floodplain harvest] is a relatively new phenonema, we struggled to find meaning the correct terminology to use when we observed the behaviour. It looks like a man-made lake but a water storage (reservoir) for floodplain harvesting is more 'edgy' with rectangular-like shapes.  

Our definition of floodplain harvesting is:
1) a man-made structure to collect and store large quantities of water on private land.
2) the purpose of the structure is to ensure enough water for a production, purely incentized on profits.  

We downloaded images from MAXAR Technologies in regions we knew water harvesting took place. From what we discovered, many of the water storages were either semi-full or empty. This imposed a problem as our original assumption was binary (yes/no) to detect a water storage, and though the images it was impossible to 'label' a water storage only based on completely full water storages.

We had our original label: reservoir
We came up with an additional label: deadspot

A deadspot is an area within the reservoir which has no water ie. the elevation is slightly higher. A reservoir can have multiple deadspots, and an empty reservoir is both a deadspot and a reservoir.
By creating this additional label our model was able to understand variations in the images that have water storages. It makes a lot more sense when seeing this on images. 

By having these two labels the model could detect whether we were observing water harvesting, or, if it was just an agricultural field with no crops. 
We were using Cogniflow.ai to get create 'areas' within the images where we observed both reservoirs and deadspots. 

The 'blind spot' in our model has been when a full water storage had a strong presence of algae booms. From satellites, when you look at a water storage that is light green it resembles a lot like the neighboring agricultural field that is being irrigated. We did not come up with a smart label/technique to identify algae booms in a reservoir, however, for the scope of the project, we would expect the chances for misinterpreting a resevoir for an agricultural field to be low.  

## Future work for laying the foundations to enhanced water governance
Water governance deals with the distribution of adequate available amount of water in a river basin. The Murray-Darling Basin holds 22,256 GL (gigalitres) of water in its entire basin. Every 1 GL represents 1,000 ML (megalitres), and a guesstimate is that water storages can vary in sizes of 5 ML to 2.000 ML. When water policy is designed it relies heavily on having a transparent and accurate water take. Although a simple behaviour of building a 2 GL water storage unit would not have an effect on the cumulative 22,256 GL it does take out local flows in a river which can cause a flow-disruption to a river system. The distribution of these water storages must be scattered out in order to avoid local resource collapses. With the help of imagery over land which detects these storages, a government can better plan and prepare for potential local water availability problems. 

A future work for this project will be to integrate sensor readings from flow rate modules with the satelite images to track exactly how much water storages (reservoirs) indivdually take from a river basin. 

## Folders
annoated_data <- here you will find test and training images
labeled_data <- we used cogniflow.ai to "identify" reservoirs and deadspots in a coordinate-like way
raw_image_data <- all our data files. Note: the name for each image are longitude and latitude coordinates, feel free to copy-paste these coordinates to find the actual locations. You can find the locations using MAXAR discover: https://discover.maxar.com/
scripts <- here you will find "split_data.py" copy-paste the code and run it on NVIDIA Jetson Nano.



### Dependencies
- Clone the repository.
- Setup the environment with the .yaml-file that has all the dependencies.
- Then open jupyter lab and run the different notebooks.

```bash
    conda env create -f  waterHarvestingDetectionNewSouthWales.yml
    conda activate waterHarvestingDetectionNewSouthWales
    jupyter-lab
```

The notebook folder contains all the code for the data analysis.
