
import '../asset/style/Team.css';
import { TeamData } from '../asset/AppData'

const Team = () => {
    return (
        <div className="app-main-team">
            <div className="tm-list">
                {TeamData.map((item, index) => (
                    <div key={index} className="tm-li">
                        <div className="tm-name">{item.name}</div>
                        <div className="tm-links">
                            {item.links.map((i, ix) => (
                                <a key={ix} href={i.link} target="_blank" rel="noopener noreferrer" className="tm-link">
                                    {i.logo()}
                                </a>
                            ))}
                        </div>
                    </div>
                ))}
            </div>
        </div>
    )
}

export default Team;
