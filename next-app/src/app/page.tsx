
import './Asset/styles.css'

let year = new Date().getFullYear()

export default function Home(params: any) {
  return (
    <div id="app">
      <div id="app-header">
        <div className='header-h1'>
          <div className='header-h2'>Major Project</div>
          Stock Prediction using ML/Data Science
        </div>
      </div>

      <div id="app-body">
        <a href='/ps'>
          <div className='btn-link'>Problem Statement</div>
        </a>

        <a href='/sol'>
          <div className='btn-link'>Solution Approach</div>
        </a>

        <a href='/pred'>
          <div className='btn-link'>Stock Predictor</div>
        </a>
      </div>

      <div id="app-footer">
        <div className='header-h3'>Devloped by <a className='link' href='/intro'>@TeamIntro</a> Copyright &copy; {year} 💝 </div>
      </div>
    </div>
  )
}
