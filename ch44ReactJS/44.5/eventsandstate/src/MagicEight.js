import {useState} from 'react';

const MagicEight = ({answers}) => {

    
    // generates a random index of the answers array  
    const generateNum = () => {
        return Math.floor((Math.random() * answers.length));
    }
    const [msg, setMsg] = useState(answers[generateNum()].msg);
    const [color, setColor] = useState('black');

    const handleClick = () => {
        const index = generateNum();
        setMsg(answers[index].msg);
        setColor(answers[index].color);
    }

    return (
        <div style={{backgroundColor: color, borderRadius: "50%", width: "300px", height: "300px", display: "flex", alignItems: "center", justifyContent: "center"}}>
            <h1 onClick={handleClick} style={{color: 'white'}}>
                {msg}
            </h1>

        </div>
    )
}


export default MagicEight;