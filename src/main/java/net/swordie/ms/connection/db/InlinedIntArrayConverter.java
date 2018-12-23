package net.swordie.ms.connection.db;


import javax.persistence.AttributeConverter;
import java.util.ArrayList;
import java.util.List;

/**
 * @author Sjonnie
 * Created on 12/19/2018.
 */
public class InlinedIntArrayConverter implements AttributeConverter<List<Integer>, String> {
    @Override
    public String convertToDatabaseColumn(List<Integer> integers) {
        StringBuilder sb = new StringBuilder();
        for (int i : integers) {
            sb.append(i).append(",");
        }
        return sb.toString().substring(0, sb.length() - 1); // removes last comma
    }

    @Override
    public List<Integer> convertToEntityAttribute(String s) {
        if (s == null) {
            return null;
        }
        String[] split = s.split(",");
        List<Integer> ints = new ArrayList<>();
        for (String str : split) {
            ints.add(Integer.valueOf(str));
        }
        return ints;
    }
}