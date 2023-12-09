
// part 1A
const firstComp = (prop) => {
    return (<h1>My very first component!</h1>)
}

// part 1B
const namedComp = (prop) => {
    return (
        <p>
            My name is {prop.name}
        </p>
    )
}

// part 1C
const app = (prop) => {
    return (<div>
        < firstComp />
        < namedComp name="Kevin" />
    </div>)
}



// part 2
const TweetLog = (prop) => {
    return (
        <div className="Styled">
            <h1>Info About Tweeter</h1>
            <h3>Username: {prop.username}</h3>
            <h3>Name: {prop.name}</h3>
            <h3>Date: {prop.date}</h3>
            <h3>Message: {prop.message}</h3>
        </div>


    )
}


const parentApp = () => {
    return (
        <div>
            <TweetLog username="joeschmoe70" name="Joe Kronas" date="03/23/22" message="I like Cheese" />
            <TweetLog username="markymarky" name="Mark Lee" date="04/22/19" message="Starlights are so 2010" />
            <TweetLog username="dunzylover" name="Sarah Parker" date="9/3/23" message="Who else is running for President?" />
            <TweetLog username="cancanaman" name="Cecilia Wozinski" date="2/3/14" message="Who?" />

        </div>
    )
}


// part 3
const Person = (props) => {
    let message = props.age >= 18 ? "Please go vote!" : "You must be 18!";
    let displayName = props.name.length > 8 ? props.name.slice(0, 6) : props.name;
    return (
        <div>
            <p>Learn some information about this person.</p>
            <p>Name: {displayName}</p>
            <p>Age: {props.age}</p>
            <h3>{message}</h3>
            <ul>
                {props.hobbies.map(hobby => <li key={hobby}>{hobby}</li>)}
            </ul>
        </div>
    );
}


const App = () => {
    return (
        <div>
            <Person name="Elizabeth" age={30} hobbies={["Reading", "Gardening"]} />
            <Person name="Johnathan" age={17} hobbies={["Gaming", "Hiking"]} />
            <Person name="Alexandria" age={20} hobbies={["Cooking", "Dancing"]} />
        </div>
    );
}
