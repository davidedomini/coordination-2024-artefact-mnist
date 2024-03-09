# coordination-2024-artifact

This repository contains the artefact associated with the regular paper entitled "Field-based Coordination for Federated Learning" and submitted at [COORDINATION'24](https://www.discotec.org/2024/coordination.html). More specifically, this artefact can be used to reproduce the experiments illustrated in the paper and related to MNIST and Fashion MNIST datasets.

## How to use
To reproduce the experiments, the following steps are needed:
- Install Docker on your machine;
- Clone this repository: `git clone git@github.com:davidedomini/coordination-2024-artefact-mnist.git`
- Move inside the repository;
- Execute the command: `docker compose up `
- Since reproducing all the learning steps could be very time consuming (~5 hours) on a normal machine we already provided the data exported from the learning. In this way it is possible to regenerate only the charts executing the following command: `docker compose run --no-deps charts`

## Authors:
- [Davide Domini](mailto:davide.domini@unibo.it)
- [Gianluca Aguzzi](mailto:gianluca.aguzzi@unibo.it)
- [Lukas Esterle](mailto:lukas.esterle@ece.au.dk)
- [Mirko Viroli](mailto:mirko.viroli@unibo.it)
