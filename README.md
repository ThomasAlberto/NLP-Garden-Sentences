# Gardenpath Sentences

This program tokenises sentences and performs entity recognition on a list of garden-path sentences.

## Installation

1. Install Docker on your system.

2. Clone the repository.

3. Build the Docker image by running the following command in the repository directory:

> docker build -t gardenpath-sentences .

4. Run the Docker container by running the following command:

> docker run -p 80:80 gardenpath-sentences

## Usage

Once the container is running, navigate to `http://localhost` in your web browser. You will see the tokenised sentences 
and the entities recognised in each sentence.

## Gardenpath Sentences

The gardenpath sentences used in this program are:

> The cotton clothing is made of grows in Mississippi.
> 
> The florist sent the bouquet of flowers was very flattered.
> 
> Because he always jogs a mile seems a short distance to him.
> 
> The prime number few.
> 
> The man who hunts ducks out on weekends.
> 
> The man who hunts ducks out on weekends.
> 
> Until the police arrest the drug dealers control the street.
>
> Fat people eat accumulates.
> 
> Mary saw the girl drank some water.