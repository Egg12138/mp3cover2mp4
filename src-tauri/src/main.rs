// Prevents additional console window on Windows in release, DO NOT REMOVE!!
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

// #[tauri::command]
// fn load_ffmpeg_env(name: &str) -> String {
//     std::env::var(String::from(name)).unwrap_or("ffmpeg".to_string())
// }

#[tauri::command]
fn run_converter(mp3name: String) -> Result<String, String> {
    use std::process::Command;
    let output = Command::new("python")
        .arg("simple-convert.py")
        .arg(&mp3name)
        .output()
        .map_err(|e| e.to_string())?;
    if let Some(song) = mp3name.strip_suffix(".mp3") {
        if output.status.success() {
            println!("{}.mp3 -> {}.mp4 successfully!", song, song);
            Ok(String::from_utf8_lossy(&output.stdout).to_string())
        } else {
            Err(String::from_utf8_lossy(&output.stderr).to_string())
        }
    } else {
        println!("Error: {}", String::from_utf8_lossy(&output.stderr));
        Err(String::from_utf8_lossy(&output.stderr).to_string())
    }
}

fn main() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![run_converter])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
