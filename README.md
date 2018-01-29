# dataset merger

This program is easy-to-setup multithread dataset merger - you should give 2 datasets, make manual calibration and get back 1 merged dataset

## Getting Started

To start the program you have to clone the repository
```
git clone https://github.com/DnyashA/datasets_merger
```
create ditectory "data" in the project and put your data there
```
cd datasets_merger
mkdir data
cp *your files* ./data
```
create a docker image
```
docker build .
```
run the container. It will make all other things automatically
```
docker run *your image name*
```
tip - use "docker images" to find image id

One more moment:
Before applying our code to your data, it'll be better to read it and add your own data handler
This process is still manual

## Deployment

To deploy our project you should have installed Docker on your x64 workstation.
So just type "docker build" in the project folder

## Built With

* [Docker](https://docs.docker.com/install/)

## Contributing

We'll take any help you can offer us for free. Please if you want to improve the project make a pool request and describe your improvements (bugfixes, fitchas, etc.)


## Authors

* **Dmitry Lossovich** - *Deployment, programming, other stuff*
* **Vladimir Chepkasov** - *Programming, research, other stuff*
* **Vladislav Basynin** - *Reseach, hardware, other stuff*

See also the list of [contributors](https://github.com/DnyashA/datasets_merger/graphs/contributors) who participated in this project.

## License

You can take it free =)