# rob599-final-project

The Wannabe Nerfs:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center"><a href="https://kentcdodds.com"><img src="https://avatars.githubusercontent.com/u/32318187?v=4" width="100px;" alt="Manu Aatitya"/><br /><sub><b>Manu Aatitya</b></sub></a><br/></td>
      <td align="center"><a href="https://github.com/jfmengels"><img src="https://user-images.githubusercontent.com/32318187/233909968-af290f97-e3bc-45ca-9821-1c6d00116195.png" width="100px;" height="120px" alt="Rohit Bannerjee"/><br /><sub><b>Rohit Bannerjee</b></sub></a><br /></td>
      <td align="center"><a href="https://jakebolam.com"><img src="https://avatars.githubusercontent.com/u/30981303?v=4" width="100px;" height="100px;" alt="Jake Bolam"/><br /><sub><b>Aravind Krishnakumar</b></sub></a><br />    
      </td>
    </tr>
    </tfbody>
</table>

## Reproduction of the NeRF Supervision Code:

- Motivation for choosing the project:
    - Inability to model shiny and reflective surfaces. Video Files using traditional techniques listed below
      
[![Hall Reconstruction](https://user-images.githubusercontent.com/32318187/233912559-2df9ab17-d3c2-472f-bcf9-2b24cddbcc5d.png)](https://www.youtube.com/watch?v=O9tI1pw5Peo) [![Fork Reconstruction](https://user-images.githubusercontent.com/32318187/233912295-21929dc1-7bc0-40f8-a0e4-b654111e2222.png)](https://www.youtube.com/watch?v=QryU3lckOUk)
      

- Have successfully reproduced the code and the results from the reproduction are as follows: 
    - Nerf Reconstruction from 200,000 iterations
    
    ![ezgif com-video-to-gif](https://user-images.githubusercontent.com/32318187/233931923-3d0bea23-e241-41a7-b224-274b8cd102f9.gif)
    
    ![depth-mamp](https://user-images.githubusercontent.com/32318187/233933598-c99f55b8-3278-4d4e-a8e9-14c144c2e515.gif)


- The pytorch dense correspondence docker image has been created from scratch for better reproduceability with all the required dependencies, since a docker image was not provided
    - [Docker Hub Link](https://hub.docker.com/r/manuaatitya/pytorch-dense-correspondence)


### New dataset tried:

- Tried on a custom shoe dataset 


<!-- - [ ] Reproduce the results
    - [ ] Figure out if the dataset is sufficient
    - [ ] If dataset is not sufficient figure out next steps
    
- [ ] Create like a flowchart or ipynb file for documentation
- [ ] Think about extension steps (later)


branches

    - master - main branch "create pull requests for any changes"
    
    branch for editing changes specific to collaborators
    
    - dev/manu
    
    - dev/rohit
    
    - dev/aravind -->
