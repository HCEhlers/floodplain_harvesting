# Project
This project is done in conenction with the Jetson AI Fundamentals course, https://developer.nvidia.com/embedded/learn/jetson-ai-certification-programs#course\_outline.

The aim of the project is to train a model that can predict - given a satellite image of agricultural areas - whether the image is a reservoir, reservoir with a dead spot
or a reservoir without a dead spot. The value of detecting water harvests autonomously (water extracted from rivers to private reservoirs) can significantly enhance water authorities' capabilities to detect potential illegal water harvesting activty in remote regions.   

## Why detecting water harvesting is important to society
Disruption to climate is causing agriculture to turn to irrigation as a safeguard for unreliable rainfall. As competition for freshwater increases, more farms are building private water storages to protect its ability to irrigate crops if a river periodically runs dry. When multiple farms creates water storages, evaporation increases - reducing both local water availability and productivity within a region. Such phenonema is known as "tragedy of the commons" and is decribed in environmental economics as an open-access and finite resource which generates value to consumers but is difficult to regulate to to its open areas. 
Such behaviour is known as water harvesting - the choice to build out dam-like infrastructure to pump water into the a privately held reservoir where no other agent can access it.  

## Satellite images to track down illegal water harvesting activity
We approached the problem of water harvesting as an authority-stakeholder-idenfication problem, on par with illigal fishery. 
Similar to fishing, imagine you catch fish, and you see your neighboring vessel using equipment (or enters forbidden zones) in order to create a larger catch. 
You have a feeling something is wrong, yet, you cannot quantify the catch and you do not have legitimate evidence that something illegal is taking place. 

The same occurs when you grow crops through irrigation, and you see your neighbor having large pumps and stores water somewhere on private property. Now, as satellites are crossing the skies, it becomes possible to gather information. Though, detecting water harvesting is not as simple as detecting a can of Coca-Cola as water storages have various sizes and forms.   

## Creating two labels and assumptions to identify water harvesting
We downloaded images from MAXAR Technologies in regions we knew water harvesting took place. From what we discovered, many of the water storages were either semi-full or empty. This imposed a problem as our original assumption was binary (yes/no) to detect a water storage, and though the images it was impossible to 'label' a water storage only based on completely full water storages.

We had our original label: reservoir
We came up with an additional label: deadspot

A deadspot is an area within the reservoir which has no water ie. the elevation is slightly higher. A reservoir can have multiple deadspots, and an empty reservoir is both a deadspot and a reservoir.
By creating this additional label our model was able to understand variations in the images that have water storages. It makes a lot more sense when seeing this on images. 

By having these two labels the model could detect whether we were observing water harvesting, or, if it was just an agricultural field with no crops. 
We were using Cogniflow.ai to get create 'areas' within the images where we observed both reservoirs and deadspots. 

The 'blind spot' in our model has been when a full water storage had a strong presence of algae booms. From satellites, when you look at a water storage that is light green it resembles a lot like the neighboring agricultural field that is being irrigated. We did not come up with a smart label/technique to identify algae booms in a reservoir, however, for the scope of the project, we would expect the chances for misinterpreting a resevoir for an agricultural field to be low.  

## Laying the foundations for the most badass water authority in the world and future work

Rarely, you come across ideas that targets megatrends in climate adaptation. Most ideas relate to carbon emissions. 


- Describe use of Cogniflow.ai for labelling data (R)
- Document assumptions used in labelling (R)
- Future work could estimation of water storage + sensor combination (R)
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
