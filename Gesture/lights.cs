using UnityEngine;

public class lights : MonoBehaviour
{
    public UDPReceive udpReceive;
    public GameObject[] lightPoints;
    public GameObject player;
    public Vector3 offset;
    void Start()
    {
        // Initialize lights or other setup if needed
    }

    void Update()
    {
        if (udpReceive.data != string.Empty)
        {
            string data = udpReceive.data;
            string[] split_data = data.Split(":");
            string command = split_data[0];
            Debug.Log("Command: " + split_data[1]);
            if (command == "Lights") {
                ControlLightsBasedOnPlayerLocation(split_data[1]);
            }
            if (command == "Intencity") { 
                ChangeIntensity(split_data[1]);
            }

            udpReceive.data = string.Empty;
        }
    }

    void ControlLightsBasedOnPlayerLocation(string data)
    {
        // Assuming data contains the command to control lights
        string playerTag = GetPlayerCurrentTag();
        if (playerTag == "Hall")
        {
            if (data == "On")
                foreach (GameObject light in lightPoints)
                {
                    if (light.CompareTag("Hall"))
                    {
                        light.SetActive(true); 
                    }
                }
            if (data == "Off")
                foreach (GameObject light in lightPoints)
                {
                    if (light.CompareTag("Hall"))
                    {
                        light.SetActive(false);  
                    }
                }
        }
        if (playerTag == "Kitchen")
        {
            if (data == "On")
                foreach (GameObject light in lightPoints)
                {
                    if (light.CompareTag("Kitchen"))
                    {
                        light.SetActive(true);
                    }
                }
            if (data == "Off")
                foreach (GameObject light in lightPoints)
                {
                    if (light.CompareTag("Kitchen"))
                    {
                        light.SetActive(false);
                    }
                }
        }

    }

    string GetPlayerCurrentTag()
    {
        // Assuming the player has a collider and is standing on a tagged block
        RaycastHit hit;
        if (Physics.Raycast(player.transform.position + offset, Vector3.down, out hit))
        {
            return hit.collider.tag;
        }
        return string.Empty;
    }

    void ChangeIntensity(string intencity) {
        float float_intencity = float.Parse(intencity);
        string playerTag = GetPlayerCurrentTag();
        if (playerTag == "Hall")
        {
            foreach (GameObject light in lightPoints)
            {
                if (light.CompareTag("Hall"))
                {
                    light.GetComponent<Light>().intensity = float_intencity;
                }
            }
        }
        if (playerTag == "Kitchen")
        {
            foreach (GameObject light in lightPoints)
            {
                if (light.CompareTag("Kitchen"))
                {
                    light.GetComponent<Light>().intensity = float_intencity;
                }
            }
        }
    }
}
