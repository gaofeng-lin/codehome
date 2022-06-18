package Factory;

import java.util.ArrayList;
import java.util.List;

public class RecommendMusicService {


    public List<String> recommend(String style) {
        List<String> recommendMusic = new ArrayList<>();

        if ("metal".equals(style)) {
            recommendMusic.add("don't cry");
        } else {
//            recommendMusic.add("my heart will go");
            recommendPop(recommendMusic);
        }
        return recommendMusic;
    }

    public void recommendPop(List<String> recommendMusic) {
        recommendMusic.add("my heart will go on");
    }



}
