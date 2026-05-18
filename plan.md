I want to build a subtitle translator, from English to Arabic

### steps to achieve this goal
1. Transcribe the video to English Subtitles
2. We want to keep the timestamps (we can use Whisper for the transcrption)
3. Save the transcription in JSON forumla
4. we want to pass the transcription into chuncks (for start, we can just pass small videos to test it)
5. translate that to Arabic with caring about the timestamps and also the subtitle length
6. we want to convert that to srt


### the design
1. we want to have models for every request and response format
2. transcription service (using Whisper)
3. divider (to divide into chunck)
4. the main driver (the orchesrsation)

### nice to have in the 30 -minutes sections (finger-crossed)
1. API endpoints
2. maybe DB
3. Queue simulation
4. rigorus error handling



### extended goals
1. add different languages
2. add dubbing
