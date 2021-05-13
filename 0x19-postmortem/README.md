#ISSUE SUMMARY
    Start   :   10:57 (GMT +2) 
    End     :   11:30 (GMT +2)
    The Web site was unavailble and return : 502 Bad Gateway on nginx/1.14.2
    The root cause was a problem of the firewall configuration for information from server <SE-102> .

#TIME LINE
    13/05/2021  10h57 :  <TEAM-OF1> An alert was issue from our monitoring tool <SAVAGE version 1.2>
                11h05 :  <TEAM-OF1> We checked is there was no physical problem on server infrastructure with TEAM <INF-01>
                11h15 :  <TEAM-OF1> We check if all port was responding and we figure the firewall was blocking the request
                11h20 :  <TEAM-OF1> We transfer the problem to the IT security team <PROX-102> to solve the problem
                11h25 :  <PROX-102> Our new employee closed all port, full check up on port and restablishement of the  communication
                11h30  :   <TEAN-OF1> Web site available, incident close

#ROOT CAUSE AND RESOLUTION 
    To solve it we checked if there was no physical problem on our server infrastructure. 
    Then we checked all port and we figure that the firewall was blocking the request.
    The PROX-102 new employee made a mistake and close all port. The resolution was to restablish the correct configuration. To do it, follow the process on </FireWall/ConfigurePort_V5.doc>

#CORRECTIVE AND PREVENTIVE ISSUE
    Improve the formation of new employee with <CP05FORM-BaseFireWall>
    Do not give full right on system without this formation
    Add warning message before validating change on the firewall.

