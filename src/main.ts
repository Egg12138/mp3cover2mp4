import './style.css'
import { invoke } from '@tauri-apps/api/tauri'
import { open } from '@tauri-apps/api/dialog'
import { writeBinaryFile } from '@tauri-apps/api/fs'

document.querySelector<HTMLDivElement>('#app')!.innerHTML = `
  <div>
    <h1>mp3+封面mp4转换器</h1>
    <div>
      <button id="selectInput">Select Input File</button>
    </div>
    <div>
      <button id="process">Process File</button>
    </div>
    <div id="status"></div>
  </div>
`

let inputFilePath: string | null = null;

document.getElementById('selectInput')!.addEventListener('click', async () => {
  const selected = await open({
    multiple: false,
    filters: [{
      name: 'mp3',
      extensions: ['mp3']
    }]
  });
  if (selected) {
    inputFilePath = selected as string;
    updateStatus('Input file selected: ' + inputFilePath);
  }
});

document.getElementById('process')!.addEventListener('click', async () => {
  if (!inputFilePath ) {
    updateStatus('Please select both input file and output location.');
    return;
  }
  
  try {
    // returned from Tauri-Rust
    const result = await invoke('run_converter', { 
      mp3name: inputFilePath,
    });
    updateStatus('Processing complete: ' + result);
  } catch (error) {
    updateStatus('Error: ' + error);
  }
});

function updateStatus(message: string) {
  document.getElementById('status')!.textContent = message;
}